import sys
import subprocess
from pathlib import Path
import os

def generate_beamer_slides(code_lines, explanations):
    """
    Generate LaTeX Beamer slides with moving spotlight on each line.
    Shows only 5 lines (2 above, current, 2 below) on each slide.
    
    Args:
        code_lines: List of code lines to display
        explanations: List of explanations for each line (same length as code_lines)
    """
    
    # Calculate vertical positions for each line in the 5-line window
    # Line positions for a 5-line display (current line is in the middle, line 3)
    base_top = -2.6
    line_height = 1.1
    
    # Header
    header = r'''\documentclass{beamer}
\usepackage{listings}
\newcommand\blank[1]{\rule[-.2ex]{#1}{.4pt}}
\usepackage{tikz}
\usetikzlibrary{shapes.callouts, positioning, arrows.meta,calc,backgrounds}
\usepackage[dvipsnames]{xcolor}

% Use plain theme with no decorations
\usetheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{}
\setbeamertemplate{headline}{}

% Define Java code style
\lstdefinestyle{JavaStyle}{
    language=Java,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue}\bfseries,
    commentstyle=\color{green!60!black},
    stringstyle=\color{Maroon},
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=10pt,
    breaklines=true,
    frame=single,
    tabsize=2,
    showstringspaces=false,
    firstnumber=auto
}

\title{Understanding Java Code Execution}
\subtitle{Step-by-Step Walkthrough}
\author{Programming Tutorial}
\date{}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

'''
    
    # Footer
    footer = r'''\end{document}'''
    
    # Generate frames
    frames = []
    num_lines = len(code_lines)
    
    for i in range(num_lines-1):
        current_line = i + 1  # 1-indexed line number
        
        # Determine which lines to show (2 above, current, 2 below)
        start_idx = max(0, i - 2)
        end_idx = min(num_lines-1, i + 3)
        visible_lines = code_lines[start_idx:end_idx]
        
        # Calculate the position of the current line within the visible window
        current_pos_in_window = i - start_idx  # 0-indexed position in visible window
        
        # Calculate window coordinates for highlighting the current line
        top = base_top - (current_pos_in_window * line_height)
        bottom = top + line_height
        
        # First line number to display
        first_line_num = start_idx + 1
        
        # Generate code content
        code_content = '\n'.join(visible_lines)
        code_content = f'\n{code_content}'
        print('Content:')
        print(code_content)
        print('is the content')
        frame = ''
        # Get explanation for current line (escape LaTeX special characters)
        if len(explanations) > 0:
            explanation = explanations[i].replace('\\', '\\textbackslash{}').replace('_', '\\_').replace('{', '\\{').replace('}', '\\}').replace('&', '\\&').replace('%', '\\%').replace('#', '\\#')

            frame = r'''\begin{frame}[fragile]{Code Execution Flow}
    \begin{center}
    \begin{tikzpicture}[remember picture, overlay]
        % Code listing (named node so we can reference its bounds)
        \node[anchor=center] (code) at (current page.center) {
            \hspace{1cm}
            \begin{minipage}{\textwidth}
    \begin{lstlisting}[style=JavaStyle,firstnumber=''' + f'{first_line_num}' + r''']
    ''' + code_content + r'''
    \end{lstlisting}
            \end{minipage}
        };
        
        % === Spotlight the current line: draw a semi-opaque overlay with a hole ===
        \begin{scope}[on background layer]
            % Compute a window rectangle around the current line
            \path let \p1=(code.north west), \p2=(code.north east) in
                coordinate (winNW) at (\x1+0.9em, \y1''' + f'{top:.1f}' + r'''em)  % top-left of the window
                coordinate (winSE) at (\x2-0.9em, \y1''' + f'{bottom:.1f}' + r'''em); % bottom-right of the window
            
            % Wash out (pseudo-blur) everything except the window using even-odd rule
            \fill[black,opacity=0.5,even odd rule]
                (code.south west) rectangle (code.north east)
                (winNW) rectangle (winSE);
            
            % Draw the red box around the visible line
            \draw[red,very thick,rounded corners=2pt] (winNW) rectangle (winSE);
        \end{scope}
        
        % Explanation box below the code
        \node[anchor=north,fill=blue!10,draw=blue!50,thick,rounded corners,
            text width=0.8\textwidth,align=left,inner sep=10pt] 
            at ($(current page.north)+(0,-1.5cm)$) {
            \textbf{Line ''' + f'{current_line}' + r''':} ''' + explanation + r'''
        };
    \end{tikzpicture}
    \end{center}
    \end{frame}

    ''' 
        else:
            frame = r'''\begin{frame}[fragile]{Code Execution Flow}
    \begin{center}
    \begin{tikzpicture}[remember picture, overlay]
        % Code listing (named node so we can reference its bounds)
        \node[anchor=center] (code) at (current page.center) {
            \hspace{1cm}
            \begin{minipage}{\textwidth}
    \begin{lstlisting}[style=JavaStyle,firstnumber=''' + f'{first_line_num}' + r''']
    ''' + code_content + r'''
    \end{lstlisting}
            \end{minipage}
        };
        
        % === Spotlight the current line: draw a semi-opaque overlay with a hole ===
        \begin{scope}[on background layer]
            % Compute a window rectangle around the current line
            \path let \p1=(code.north west), \p2=(code.north east) in
                coordinate (winNW) at (\x1+0.9em, \y1''' + f'{top:.1f}' + r'''em)  % top-left of the window
                coordinate (winSE) at (\x2-0.9em, \y1''' + f'{bottom:.1f}' + r'''em); % bottom-right of the window
            
            % Wash out (pseudo-blur) everything except the window using even-odd rule
            \fill[black,opacity=0.5,even odd rule]
                (code.south west) rectangle (code.north east)
                (winNW) rectangle (winSE);
            
            % Draw the red box around the visible line
            \draw[red,very thick,rounded corners=2pt] (winNW) rectangle (winSE);
        \end{scope}
    \end{tikzpicture}
    \end{center}
    \end{frame}

    ''' 

        frames.append(frame)
    
    # Combine all parts
    full_document = header + ''.join(frames) + footer
    
    return full_document


def read_java_file(filename):
    """Read a Java file and return its lines."""
    try:
        with open(filename, 'r') as f:
            return [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def read_explanations_file(filename, num_lines=30):
    """
    Read explanations from a file. 
    File should have one explanation per line, matching the Java file line-by-line.
    If file doesn't exist or has fewer lines, use default explanations.
    """
    explanations = []
    
    try:
        with open(filename, 'r') as f:
            explanations = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"Warning: Explanations file '{filename}' not found. Using default explanations.")
        explanations = []
    except Exception as e:
        print(f"Warning: Error reading explanations file: {e}. Using default explanations.")
        explanations = []
    
    # Pad with default explanations if needed
    while len(explanations) < num_lines:
        line_num = len(explanations) + 1
        explanations.append(f"Executing line {line_num}")
    
    # Truncate if too many explanations
    return explanations[:num_lines]


# Main execution
if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <java_file> [explanations_file]")
        print("Example: python script.py Main.java")
        print("Example: python script.py Main.java explanations.txt")
        sys.exit(1)
    
    java_file = sys.argv[1]
    explanations_file = sys.argv[2] if len(sys.argv) == 3 else None
    
    # Read the Java file
    code_lines = read_java_file(java_file)
    
    if not code_lines:
        print("Error: The Java file is empty.")
        sys.exit(1)
    
    # Read explanations
    if explanations_file:
        explanations = read_explanations_file(explanations_file, len(code_lines))
    else:
        # Use default explanations
        explanations = [f"Executing line {i+1}" for i in range(len(code_lines))]
        explanations = []
    
    # Generate the slides
    latex_output = generate_beamer_slides(code_lines, explanations)
    
    # Save to file
    output_file = "slides.tex"
    with open(output_file, "w") as f:
        f.write(latex_output)

    print(latex_output)
    
    print(f"LaTeX slides generated successfully!")
    print(f"Input: {java_file} ({len(code_lines)} lines)")
    if explanations_file:
        print(f"Explanations: {explanations_file}")
    print(f"Output: {output_file}")
    print(f"Created {len(code_lines)} execution slides (plus title slide)")
    print(f"\nCompile with: pdflatex {output_file}")
    #os.system("/Library/TeX/texbin/pdflatex slides.tex")
    #os.system("../clean-dir.sh .")