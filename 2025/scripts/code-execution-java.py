import sys
import subprocess
from pathlib import Path

def generate_beamer_slides(code_lines):
    """
    Generate LaTeX Beamer slides with moving spotlight on each line.
    Shows only 5 lines (2 above, current, 2 below) on each slide.
    
    Args:
        code_lines: List of code lines to display
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
\usepackage[dvipsnames]{xcolor}
\usetikzlibrary{shapes.callouts, positioning, arrows.meta,calc,backgrounds}

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
        end_idx = min(num_lines, i + 3)
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


# Main execution
if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <java_file>")
        print("Example: python script.py Main.java")
        sys.exit(1)
    
    java_file = sys.argv[1]
    
    # Read the Java file
    code_lines = read_java_file(java_file)
    
    if not code_lines:
        print("Error: The Java file is empty.")
        sys.exit(1)
    
    # Generate the slides
    latex_output = generate_beamer_slides(code_lines)
    
    # Save to file
    output_file = "slides.tex"
    with open(output_file, "w") as f:
        f.write(latex_output)
    
    print(f"LaTeX slides generated successfully!")
    print(f"Input: {java_file} ({len(code_lines)} lines)")
    print(f"Output: {output_file}")
    print(f"Created {len(code_lines)} execution slides (plus title slide)")
    print(f"\nCompile with: pdflatex {output_file}")
    