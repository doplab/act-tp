# -*- coding: utf-8 -*-
'''
@author: Amro Abdrabo
@date: 2025-09-25
@description: This script generates a LaTeX TikZ diagram showing the division by 2 process.
@usage: python gen_division_diagram.py <number>
@example: python gen_division_diagram.py 113 20
@output: division_by_2_113.tex
@output: division_by_2_20.tex
'''

import sys
def generate_division_by_2_diagram(number):
    """
    Generate a LaTeX TikZ diagram showing division by 2 process.
    
    Args:
        number (int): The number to divide by 2 repeatedly
    
    Returns:
        str: LaTeX code for the TikZ diagram
    """
    
    # Calculate the division steps
    steps = []
    current = number
    
    while current > 0:
        remainder = current % 2
        quotient = current // 2
        steps.append({
            'dividend': current,
            'quotient': quotient,
            'remainder': remainder,
            'subtracted': current - remainder
        })
        current = quotient
    
    # Building the LaTeX code
    latex_code = r"""\documentclass{article}
\usepackage{tikz}
\usepackage{array}
\usetikzlibrary{arrows.meta}
\usepackage{booktabs}
\def\x{1}
\def\y{1}
% Define column type for centered text with specified width
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}
\begin{document}
\begin{tikzpicture}[scale=1.3]
    % Ladder pattern: vertical down, horizontal right, vertical down, horizontal right, etc."""
    
    # Generate the diagram elements
    nodes_coords = []  # Store coordinates of remainder nodes for red arrows
    
    for i, step in enumerate(steps):
        x_pos = i
        y_start = 4 - i
        y_mid = y_start - 1
        
        # Vertical line down
        latex_code += f"\n    \\draw[thick] ({x_pos},{y_start}) -- ({x_pos},{y_mid});        % vertical down"
        
        # Dividend label
        latex_code += f"\n    \\node[left] at ({x_pos},{y_start - 0.5}) {{\\Huge {step['dividend']}}};)"
        
        # Subtracted value and remainder
        latex_code += f"\n    \\node[left] at ({x_pos},{y_mid - 0.5}) {{\\Huge -{step['subtracted']}}};)"
        latex_code += f"\n    \\node[right, draw=blue, thick, inner sep=2pt] at ({x_pos + 0.2}-\\x,{y_mid - 0.5}-\\y) {{\\Large R:{step['remainder']}}};)"
        
        # Store coordinates for red arrows
        nodes_coords.append(f"({x_pos + 0.2}-\\x,{y_mid - 0.5}-\\y)")
        
        # If not the last step, add horizontal line and quotient
        if i < len(steps) - 1:
            latex_code += f"\n    \\draw[thick] ({x_pos},{y_mid}) -- ({x_pos + 1},{y_mid});        % horizontal right"
            latex_code += f"\n    \\node[above] at ({x_pos + 0.5},{y_mid}) {{\\Huge 2}};"
            latex_code += f"\n    \\node[left] at ({x_pos + 1},{y_mid - 0.5}) {{\\Huge {step['quotient']}}};)"
    
    # Add the final quotient (0)
    final_x = len(steps)
    final_y = 4 - len(steps)
    latex_code += f"\n    \\node[left] at ({final_x},{final_y - 0.5}) {{\\Huge 0}};"
    
    # Add coordinates for red arrow connections
    latex_code += "\n    \n    % Red curves connecting all blue border nodes"
    latex_code += "\n    % Define the positions of the blue border nodes"
    
    for i, coord in enumerate(nodes_coords):
        latex_code += f"\n    \\coordinate (node{i+1}) at {coord};"
    
    # Add red arrows between consecutive nodes
    latex_code += "\n    \n    % Connect nodes with red curves"
    for i in range(len(nodes_coords) - 1):
        latex_code += f"\n    \\draw[red, thick, bend right=40, -{{Stealth[length=8pt,width=6pt]}}] (node{i+1}) to (node{i+2});"
    
    # Close the TikZ environment
    latex_code += "\n    \n\\end{tikzpicture}\n\\end{document}"
    
    return latex_code


def save_diagram_to_file(number, filename=None):
    """
    Generate and save the diagram to a .tex file.
    
    Args:
        number (int): The number to divide by 2
        filename (str, optional): Output filename. Defaults to 'division_by_2_{number}.tex'
    """
    if filename is None:
        filename = f"division_by_2_{number}.tex"
    
    latex_code = generate_division_by_2_diagram(number)
    
    with open(filename, 'w') as f:
        f.write(latex_code)
    
    print(f"Diagram saved to {filename}")
    return filename


# Example usage and testing
if __name__ == "__main__":
    # # Test with the example number 45
    # print("Generating division by 2 diagram for 45:")
    # diagram_45 = generate_division_by_2_diagram(45)
    # print("\nLaTeX code generated successfully!")
    
    # # Save to file
    # save_diagram_to_file(45)
    
    # Test with other numbers
    # test_numbers = [23, 16, 100]
    if len(sys.argv) < 2 or not sys.argv[1].isnumeric():
        print('Please enter one or more positive integers')
        sys.exit()

    test_numbers = [int(arg) for arg in sys.argv[1:]]
    for num in test_numbers:
        print(f"\nGenerating diagram for {num}...")
        save_diagram_to_file(num)
    
    # Show the process for a smaller number for verification
    print("\nDivision steps for 45:")
    current = int(sys.argv[1])
    step = 1
    while current > 0:
        remainder = current % 2
        quotient = current // 2
        print(f"Step {step}: {current} � 2 = {quotient} remainder {remainder}")
        current = quotient
        step += 1