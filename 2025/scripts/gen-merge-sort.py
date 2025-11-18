import sys

def generate_merge_sort_latex(data):
    """
    Generates LaTeX Beamer code for visualizing Merge Sort on a list of 8 elements.
    
    Args:
        data (list): A list of 8 elements (numbers or strings).
        
    Returns:
        str: Complete LaTeX code ready to be compiled.
    """
    if len(data) != 8:
        raise ValueError("Input list must have exactly 8 elements.")

    # Helper to format lists for LaTeX (removes spaces for tight formatting)
    def fmt_list(lst):
        return str(lst).replace(" ", "")

    # 1. Precompute node data (input slice and sorted result)
    # We define the tree structure manually to match the 8-element recursion.
    # Structure tuples: (node_id, start_index, end_index)
    structure = [
        ('root', 0, 8),
        ('left', 0, 4),   ('right', 4, 8),
        ('leftA', 0, 2),  ('leftB', 2, 4),  ('rightA', 4, 6),  ('rightB', 6, 8),
        ('leftA1', 0, 1), ('leftA2', 1, 2), ('leftB1', 2, 3), ('leftB2', 3, 4),
        ('rightA1', 4, 5),('rightA2', 5, 6),('rightB1', 6, 7), ('rightB2', 7, 8),
    ]
    
    node_data = {}
    for nid, start, end in structure:
        sub = data[start:end]
        node_data[nid] = {
            'input': fmt_list(sub),
            'sorted': fmt_list(sorted(sub))
        }

    # 2. Define LaTeX Positions and Parent relations
    # These position strings are copied exactly from the reference main.tex
    # format: (parent_id, latex_position_string, is_leaf_node)
    nodes_def = {
        'root':   (None, 'at (1,5)', False),
        'left':   ('root', 'below left=\\edgelen and \\edgelen of root', False),
        'right':  ('root', 'below right=\\edgelen and \\edgelen of root', False),
        'leftA':  ('left', 'below=0.6cm of left, xshift=-2cm', False),
        'leftB':  ('left', 'below=0.6cm of left, xshift=2cm', False),
        'rightA': ('right', 'below=0.6cm of right, xshift=-2cm', False),
        'rightB': ('right', 'below=0.6cm of right, xshift=2cm', False),
        # Leaves use a larger vertical distance (3.5cm) and footnote size
        'leftA1': ('leftA', 'below=3.5cm of leftA, xshift=-1cm', True),
        'leftA2': ('leftA', 'below=3.5cm of leftA, xshift=1cm', True),
        'leftB1': ('leftB', 'below=3.5cm of leftB, xshift=-1cm', True),
        'leftB2': ('leftB', 'below=3.5cm of leftB, xshift=1cm', True),
        'rightA1':('rightA', 'below=3.5cm of rightA, xshift=-1cm', True),
        'rightA2':('rightA', 'below=3.5cm of rightA, xshift=1cm', True),
        'rightB1':('rightB', 'below=3.5cm of rightB, xshift=-1cm', True),
        'rightB2':('rightB', 'below=3.5cm of rightB, xshift=1cm', True),
    }

    # 3. Define the Schedule (14 Steps)
    # Each step defines:
    #   - Which nodes are VISIBLE (box is drawn)
    #   - Which nodes have RETURNED (blue return value is shown)
    # This follows the exact depth-first trace from the reference PDF.
    steps = [
        # Step 1: Root only
        (['root'], []),
        # Step 2: Left call
        (['root', 'left'], []),
        # Step 3: Left->Left call
        (['root', 'left', 'leftA'], []),
        # Step 4: Left->Left->Left (leaf returns)
        (['root', 'left', 'leftA', 'leftA1'], ['leftA1']),
        # Step 5: Left->Left->Right (leaf returns), Left->Left (merge returns)
        (['root', 'left', 'leftA', 'leftA1', 'leftA2'], ['leftA1', 'leftA2', 'leftA']),
        # Step 6: Left->Right call
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB'], ['leftA1', 'leftA2', 'leftA']),
        # Step 7: Left->Right->Left (leaf returns)
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1'], ['leftA1', 'leftA2', 'leftA', 'leftB1']),
        # Step 8: Left->Right->Right (leaf), Left->Right (merge), Left (merge)
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left']),
        # Step 9: Right call
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2', 'right'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left']),
        # Step 10: Right->Left call
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2', 'right', 'rightA'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left']),
        # Step 11: Right->Left->Left (leaf returns)
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2', 'right', 'rightA', 'rightA1'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left', 'rightA1']),
        # Step 12: Right->Left->Right (leaf), Right->Left (merge)
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2', 'right', 'rightA', 'rightA1', 'rightA2'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left', 'rightA1', 'rightA2', 'rightA']),
        # Step 13: Right->Right call
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2', 'right', 'rightA', 'rightA1', 'rightA2', 'rightB'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left', 'rightA1', 'rightA2', 'rightA']),
        # Step 14: Right->Right->Left/Right (leaves), Right->Right (merge), Right (merge), Root (merge)
        (['root', 'left', 'leftA', 'leftA1', 'leftA2', 'leftB', 'leftB1', 'leftB2', 'right', 'rightA', 'rightA1', 'rightA2', 'rightB', 'rightB1', 'rightB2'], ['leftA1', 'leftA2', 'leftA', 'leftB1', 'leftB2', 'leftB', 'left', 'rightA1', 'rightA2', 'rightA', 'rightB1', 'rightB2', 'rightB', 'right', 'root']),
    ]

    # 4. Standard Header/Preamble
    latex = r"""\documentclass[aspectratio=169]{beamer}
\usepackage{listings}
\usepackage{listings}
\usepackage{xcolor}
\newlength{\edgelen}
\setlength{\edgelen}{0.3cm}
\newcommand\blank[1]{\rule[-.2ex]{#1}{.4pt}}
\usepackage{tikz}
\usetikzlibrary{shapes,arrows,positioning}
\usepackage[dvipsnames]{xcolor}

\usetikzlibrary{shapes.callouts, positioning, arrows.meta,calc,backgrounds}

% Use plain theme with no decorations
\usetheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{}
\setbeamertemplate{headline}{}

% Define Java code style
\lstdefinestyle{pythonstyle}{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue}\bfseries,
    commentstyle=\color{gray}\itshape,
    stringstyle=\color{red},
    numberstyle=\tiny\color{gray},
    numbers=left,
    stepnumber=1,
    numbersep=8pt,
    backgroundcolor=\color{white},
    showspaces=false,
    showstringspaces=false,
    showtabs=false,
    frame=single,
    tabsize=4,
    captionpos=b,
    breaklines=true,
    breakatwhitespace=false
}

\title{Tri par fusion - Récursion illustrée}
\subtitle{Étapes de la récursion}
\author{Algorithmes et Pensée Computationnelle \newline \newline  {\small UNIL — École des Sciences Criminelles}}
\date{}

\begin{document}

\begin{frame}
\titlepage
\end{frame}

\begin{frame}[fragile]{Code}
\begin{center}
\begin{lstlisting}[style=pythonstyle, caption={Merge sort — Python}]
def sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = sort(arr[:mid])
    right = sort(arr[mid:])
    
    return merge(left, right)
\end{lstlisting}
\end{center}

La fonction \texttt{merge} prend deux listes triées comme paramètres et renvoient une liste triée qui est la fusion de ces deux listes. La fonction \texttt{merge} a donc une complexité de $O(n)$.
\end{frame}
"""

    # 5. Generate Code for Each Step
    for i, (visible, returned) in enumerate(steps, 1):
        
        # Configuration per frame
        # Frame 1 uses a smaller bounding box and wider Root node
        if i == 1:
            bbox = r"\draw[draw = white] (-7,-4) rectangle (7,4);  % invisible bounding box"
            resize_cmd = r"\resizebox{0.92\textwidth}{!}{%"
        else:
            bbox = r"\draw[draw = white] (-7,-6) rectangle (7,6);  % invisible bounding box"
            # Frames 13+ are slightly wider in the reference
            if i >= 13:
                resize_cmd = r"\resizebox{1.02\textwidth}{!}{%"
            else:
                resize_cmd = r"\resizebox{0.92\textwidth}{!}{%"

        latex += f"""
\\begin{{frame}}[fragile]{{Étape {i}}}

{resize_cmd}
\\begin{{tikzpicture}}[
    node distance=1cm,
    box/.style={{rectangle, draw=black, thick,
                minimum width=1cm, minimum height=1cm, align=center}}
]

{bbox}

"""
        
        # To ensure parent nodes are usually drawn/defined before children (good practice for TikZ)
        # we iterate through our structure definition order, checking visibility.
        nodes_order = [n[0] for n in structure]
        
        for nid in nodes_order:
            if nid not in visible:
                continue

            parent, pos_str, is_leaf = nodes_def[nid]
            input_val = node_data[nid]['input']
            
            # Logic for return value label
            if is_leaf:
                ret_label = "ret:"
                font_mod = "\\footnotesize"
            else:
                ret_label = "return:"
                font_mod = ""

            if nid in returned:
                # \!\!\!\! is used in the reference to remove whitespace after return:
                ret_val = f"\\!\\!\\!\\! {node_data[nid]['sorted']}"
            else:
                ret_val = ""

            # Build Node Content
            # We insert the text content including the blue return text
            if is_leaf:
                # Leaf nodes have the font modifier inside the node content
                node_text = f"""{font_mod}
 \\texttt{{\\shortstack[l]{{sort({input_val}) \\\\ \\textcolor{{blue}}{{{ret_label}{ret_val}}}}}}}"""
            else:
                node_text = f""" \\texttt{{\\shortstack[l]{{sort({input_val}) \\\\ \\textcolor{{blue}}{{{ret_label}{ret_val}}}}}}}"""
            
            latex += f"\\node[box, {pos_str}] ({nid}) {{{node_text}\n}};\n" if parent else f"\\node[box] ({nid}) {pos_str} {{{node_text}\n}};\n"

            # Draw Edge from Parent
            if parent and parent in visible:
                latex += f"\\draw[->, very thick] ({parent}) -- ({nid});\n"

        latex += "\\end{tikzpicture}\n}\n\\end{frame}\n"

        # Special fix for Frame 1: Root node is wider (3cm) in the reference
        if i == 1:
            latex = latex.replace("minimum width=1cm", "minimum width=3cm")

    latex += "\n\\end{document}"
    return latex

# Example Usage
if __name__ == "__main__":
    # You can change this list to any 8 items (numbers or strings)
    example_list = [10, 5, 8, 46, 3, 9, 2, 2]
    
    try:
        print(generate_merge_sort_latex(example_list))
    except ValueError as e:
        print(e)