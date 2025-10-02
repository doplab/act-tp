from typing import List, Optional, Tuple, Literal

ArrowType = Literal["straight", "curved", None]

class StackDiagramGenerator:
    """
    Generate TikZ stack diagrams with customizable parameters.
    
    Parameters:
    - num_rectangles: Number of rectangles in the stack
    - gray_indices: List of indices (0-based from top) to be grayed out
    - bracket_text: Text to display next to the brace
    - variables: List of variable names for non-gray rectangles (None for gray ones)
    - labels: List of labels to display inside each rectangle
    - arrows: List of arrow types for each rectangle ("straight", "curved", or None)
    """
    
    def __init__(self, width: float = 4.0, height: float = 1.0):
        self.width = width
        self.height = height
    
    def generate(self, 
                 num_rectangles: int,
                 gray_indices: List[int],
                 bracket_text: str,
                 variables: List[Optional[str]],
                 labels: List[str],
                 arrows: Optional[List[ArrowType]] = None) -> str:
        """
        Generate the complete LaTeX/TikZ code for a stack diagram.
        
        Args:
            num_rectangles: Total number of rectangles
            gray_indices: Indices of rectangles to fill gray (0-based from top)
            bracket_text: Text for the brace annotation
            variables: Variable names for each rectangle (None for gray ones)
            labels: Labels inside each rectangle
            arrows: Arrow types for each rectangle ("straight", "curved", or None)
        
        Returns:
            Complete LaTeX document as a string
        """
        
        if len(variables) != num_rectangles:
            raise ValueError(f"variables list must have {num_rectangles} elements")
        if len(labels) != num_rectangles:
            raise ValueError(f"labels list must have {num_rectangles} elements")
        if arrows is not None and len(arrows) != num_rectangles:
            raise ValueError(f"arrows list must have {num_rectangles} elements")
        
        if arrows is None:
            arrows = [None] * num_rectangles
        
        # Start building the TikZ picture
        rectangles = self._generate_rectangles(num_rectangles)
        gray_fills = self._generate_gray_fills(gray_indices)
        label_nodes = self._generate_labels(labels, num_rectangles)
        variable_nodes = self._generate_variables(variables, num_rectangles)
        arrow_nodes = self._generate_arrows(arrows, num_rectangles)
        brace = self._generate_brace(num_rectangles, bracket_text)
        
        # Combine all parts
        tikz_content = rectangles + gray_fills + label_nodes + variable_nodes + arrow_nodes + brace
        
        # Wrap in document structure
        return self._wrap_document(tikz_content)
    
    def _generate_rectangles(self, num: int) -> str:
        """Generate rectangle drawing commands."""
        code = "  % Draw the stack rectangles\n"
        for i in range(num):
            y_top = -i * self.height
            y_bottom = -(i + 1) * self.height
            code += f"  \\draw (0,{y_top}) rectangle ({self.width},{y_bottom});\n"
        return code + "\n"
    
    def _generate_gray_fills(self, indices: List[int]) -> str:
        """Generate gray fill commands for specified indices."""
        if not indices:
            return ""
        
        code = "  % Fill gray areas\n"
        for idx in indices:
            y_top = -idx * self.height
            y_bottom = -(idx + 1) * self.height
            code += f"  \\fill[gray!50] (0,{y_top}) rectangle ({self.width},{y_bottom});\n"
        return code + "\n"
    
    def _generate_labels(self, labels: List[str], num: int) -> str:
        """Generate label nodes inside rectangles."""
        code = "  % Labels inside rectangles\n"
        for i in range(num):
            y_center = -i * self.height - self.height / 2
            code += f"  \\node at ({self.width/2},{y_center}) {{{labels[i]}}};\n"
        return code + "\n"
    
    def _generate_variables(self, variables: List[Optional[str]], num: int) -> str:
        """Generate variable name nodes for non-gray rectangles."""
        code = "  % Variable names on left\n"
        for i in range(num):
            if variables[i] is not None:
                y_center = -i * self.height - self.height / 2
                code += f"  \\node[anchor=east, text=red!70!black, font=\\bfseries] at (0,{y_center}) {{{variables[i]}}};\n"
        return code + "\n"
    
    def _generate_arrows(self, arrows: List[ArrowType], num: int) -> str:
        """Generate arrow commands for specified rectangles."""
        code = "  % Arrows on left side\n"
        has_arrows = False
        
        for i in range(num):
            if arrows[i] == "straight":
                has_arrows = True
                # Straight arrow pointing up
                y_center = -i * self.height - self.height / 2
                y_start = y_center - 0.3
                y_end = y_center + 0.3
                code += f"  \\draw[->, thick] (-0.5,{y_start}) -- (-0.5,{y_end});\n"
            elif arrows[i] == "curved":
                has_arrows = True
                # Curved arrow (arc from bottom)
                y_center = -i * self.height - self.height / 2
                code += f"  \\draw[->, thick] (-0.5,{y_center}) arc(-90:-180:0.3);\n"
        
        return code + "\n" if has_arrows else ""
    
    def _generate_brace(self, num: int, text: str) -> str:
        """Generate brace with annotation text."""
        y_top = 0
        y_bottom = -num * self.height
        code = "  % Bracket for annotation\n"
        code += f"  \\draw[decorate,decoration={{brace,amplitude=5pt,mirror}}]\n"
        code += f"    ({self.width},{y_bottom}) -- ({self.width},{y_top}) node[midway,xshift=2.2cm,text width=3.5cm,align=left]\n"
        code += f"    {{{text}}};\n"
        return code
    
    def _wrap_document(self, tikz_content: str) -> str:
        """Wrap TikZ content in a complete LaTeX document."""
        return f"""\\documentclass[tikz,border=5pt]{{standalone}}
\\usetikzlibrary{{positioning,decorations.pathreplacing}}
\\begin{{document}}
\\begin{{tikzpicture}}[font=\\sffamily]
{tikz_content}
\\end{{tikzpicture}}
\\end{{document}}"""


# Example usage
if __name__ == "__main__":
    generator = StackDiagramGenerator()
    
    # Example 1: Original diagram with arrows
    print("=== Example 1: Original Stack Diagram with Arrows ===")
    latex_code1 = generator.generate(
        num_rectangles=4,
        gray_indices=[2, 3],  # Third and fourth rectangles (0-indexed)
        bracket_text="stack frame of \\\\ \\textit{\\textbf{\\textcolor{violet}{main}}} program",
        variables=["year", "args", None, None],  # None for gray rectangles
        labels=["2000", "$[\\,]$", "", ""],
        arrows=[None, None, "straight", "curved"]  # Arrows on gray rectangles
    )
    print(latex_code1)
    print("\n")
    
    # Example 2: Function call stack with arrows
    print("=== Example 2: Function Call Stack with Arrows ===")
    latex_code2 = generator.generate(
        num_rectangles=5,
        gray_indices=[4],
        bracket_text="stack frame of \\\\ \\textit{\\textbf{\\textcolor{blue}{calculate}}} function",
        variables=["result", "x", "y", "temp", None],
        labels=["42", "10", "32", "0", ""],
        arrows=[None, "straight", None, "straight", "curved"]
    )
    print(latex_code2)
    print("\n")
    
    # Example 3: Simple stack with no gray areas or arrows
    print("=== Example 3: Simple Stack (No Gray Areas or Arrows) ===")
    latex_code3 = generator.generate(
        num_rectangles=3,
        gray_indices=[],
        bracket_text="local variables",
        variables=["name", "age", "city"],
        labels=["'Alice'", "25", "'NYC'"]
    )
    print(latex_code3)
    
    # Save to file
    output_file = "stack.tex"
    with open(output_file, "w") as f:
        f.write(latex_code2)