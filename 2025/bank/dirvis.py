import re

def fix_tikz_nodes(latex_code):
    """
    Remove backslash before 'node' when it appears inside a 'child' block.
    
    Args:
        latex_code: String containing the LaTeX code
        
    Returns:
        Fixed LaTeX code with \node replaced by node inside child blocks
    """
    # Pattern to match \node that appears after 'child {' with optional whitespace
    # This looks for: child { followed by optional whitespace, then \node
    pattern = r'(child\s*\{\s*)\\node'
    
    # Replace \node with node (removing the backslash)
    fixed_code = re.sub(pattern, r'\1node', latex_code)
    
    return fixed_code

def generate_latex_tree(structure, root_name=None):
    """
    Generate LaTeX code for a directory tree visualization.
    
    Args:
        structure: Nested dict representing directory structure.
                  Keys starting with '/' are directories, others are files.
                  Empty string values indicate files, dict values indicate subdirectories.
        root_name: Optional root node name. If None, uses the first key.
    
    Returns:
        str: Complete LaTeX document as a string.
    """
    
    def count_nodes(node):
        """Count total nodes in a subtree (for missing children calculation)."""
        if isinstance(node, str):
            return 1
        count = 1
        for child in node.values():
            count += count_nodes(child)
        return count
    
    def generate_node(name, content, indent=1):
        """Generate LaTeX code for a single node and its children."""
        indent_str = "    " * indent
        is_dir = isinstance(content, dict)
        
        # Determine node style
        if is_dir:
            node_line = f"{indent_str}\\node [selected] {{\\faFolder[regular] {name}}}"
        else:
            node_line = f"{indent_str}\\node [file] {{\\faFile[regular] {name}}}"
        
        if not is_dir or len(content) == 0:
            return node_line
        
        # Process children
        lines = [node_line]
        children = list(content.items())
        
        for i, (child_name, child_content) in enumerate(children):
            lines.append(f"{indent_str}child {{ ")
            lines.append(generate_node(child_name, child_content, indent + 1))
            lines.append(f"{indent_str}}}")
            
            # Add missing children for proper spacing
            if i < len(children) - 1:
                missing_count = count_nodes(child_content) - 1
                for _ in range(missing_count):
                    lines.append(f"{indent_str}child [missing] {{}}")
        
        return "\n".join(lines)
    
    # Get root
    if root_name is None:
        if not structure:
            raise ValueError("Structure cannot be empty")
        root_name = list(structure.keys())[0]
        root_content = structure[root_name]
    else:
        root_content = structure
    
    # Generate the tree
    tree_content = generate_node(root_name, root_content, indent=0)
    
    # Build complete LaTeX document
    latex_doc = r"""\documentclass[tikz,border=10pt]{standalone}
\usepackage{tikz}
\usepackage{fontawesome6}
\usetikzlibrary{arrows.meta}
\usetikzlibrary{decorations.pathreplacing}
\usepackage[dvipsnames]{xcolor}
\usetikzlibrary{trees}
\begin{document}
\begin{tikzpicture}[scale=1.6,
    every node/.style = {draw=black, thick, anchor=west},
    selected/.style = {draw=OliveGreen, fill=green!30},
    file/.style = {draw=blue, fill=cyan!30},
    optional/.style = {dashed, fill=gray!50},
    grow via three points={one child at (0.5,-0.7) and two children at (0.5,-0.7) and (0.5,-1.4)},
    edge from parent path={(\tikzparentnode.south) |- (\tikzchildnode.west)}
]
"""
    
    latex_doc += tree_content + ";\n"
    latex_doc += r"""\end{tikzpicture}
\end{document}"""
    
    return latex_doc


def save_diagram_to_file(latex_code, dict, filename=None):
    """
    Generate and save the diagram to a .tex file.
    
    """
    if not filename:
        filename = f"dir_vis_output_{str(hash(latex_code))[1:4]}.tex"
    
    with open(filename, 'w') as f:
        f.write(latex_code)
    
    print(f"Diagram saved to {filename}")
    return filename

# Example usage
if __name__ == "__main__":
    # Example 1: Your original structure
    # structure1 = {
    #     '/User': {
    #         '/public': {
    #             'esc.png': ''
    #         },
    #         '/src': {
    #             'Main.class': '',
    #             'Main.java': ''
    #         },
    #         'index.html': ''
    #     }
    # }
    
    # Example 2: More complex structure
    # structure2 = {
    #     '/project': {
    #         '/docs': {
    #             'README.md': '',
    #             'guide.pdf': ''
    #         },
    #         '/src': {
    #             '/components': {
    #                 'Header.jsx': '',
    #                 'Footer.jsx': ''
    #             },
    #             'App.js': '',
    #             'index.js': ''
    #         },
    #         '/tests': {
    #             'test.py': ''
    #         },
    #         'package.json': '',
    #         '.gitignore': ''
    #     }
    # }

    lea_structure = {
        '/User': {
            '/Cours': {
                '/Cours\_1': {
                    'Slides\_1.pdf': ''
                }
            },
            '/TPs' :{
                '/Solutions': { }, 
                'tp1.py' : '',
                'tp1.java' : '',
            },
            '/Documents' : { },
            '/Photos': { }
        }
    }

    latex_code3 = fix_tikz_nodes(generate_latex_tree(lea_structure))
    save_diagram_to_file(latex_code3, lea_structure)

    print(latex_code3)