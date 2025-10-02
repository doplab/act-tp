def generate_beamer_slides(code_lines, start_line=1):
    """
    Generate LaTeX Beamer slides with moving spotlight on each line.
    
    Args:
        code_lines: List of code lines to display
        start_line: Starting line number for highlighting (1-indexed)
    """
    
    # Calculate vertical positions for each line
    # Based on the pattern: line 1: -2.6em to -1.5em, line 2: -3.7em to -2.6em, etc.
    # Each line is approximately 1.1em apart
    base_top = -1.5
    line_height = 1.1
    
    # Header
    header = r'''\documentclass{beamer}
\usepackage{listings}
\newcommand\blank[1]{\rule[-.2ex]{#1}{.4pt}}
\usepackage{tikz}
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
    stringstyle=\color{orange},
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=10pt,
    breaklines=true,
    frame=single,
    tabsize=2,
    showstringspaces=false
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
    
    # Generate code listing content
    code_content = '\n'.join(code_lines)
    
    # Generate frames
    frames = []
    num_lines = len(code_lines)
    
    for i in range(num_lines):
        line_num = i + 1
        # Calculate window coordinates for this line
        top = base_top - (i * line_height)
        bottom = top + line_height
        
        frame = r'''\begin{frame}[fragile]{Code Execution Flow}
\begin{center}
\begin{tikzpicture}[remember picture, overlay]
    % Code listing (named node so we can reference its bounds)
    \node[anchor=center] (code) at (current page.center) {
        \hspace{1cm}
        \begin{minipage}{\textwidth}
\begin{lstlisting}[style=JavaStyle]
''' + code_content + r'''
\end{lstlisting}
        \end{minipage}
    };
    
    % === Spotlight the ''' + f'{line_num}' + r'''th line: draw a semi-opaque overlay with a hole ===
    \begin{scope}[on background layer]
        % Compute a window rectangle around line ''' + f'{line_num}' + r'''
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


# Example usage
if __name__ == "__main__":
    # Sample Java code
    code = [
        "public class Main {",
        "    public static void main(String[] args) {",
        "        System.out.println(\"Hello World: 1\");",
        "        System.out.println(\"Hello World: 2\");",
        "        System.out.println(\"Hello World: 3\");",
        "        System.out.println(\"Hello World: 4\");",
        "    }",
        "}"
    ]
    
    # Generate the slides
    latex_output = generate_beamer_slides(code)
    
    # Save to file
    with open("slides.tex", "w") as f:
        f.write(latex_output)
    
    print("LaTeX slides generated successfully!")
    print(f"Created {len(code)} execution slides (plus title slide)")
    print("Compile with: pdflatex slides.tex")