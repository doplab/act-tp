#!/bin/bash

# Script to generate PDFs with different LaTeX conditional settings for a specific week directory
# Usage: ./generate_pdfs.sh <week_directory>
# Example: ./generate_pdfs.sh week01

#BASE_DIR="$HOME/Documents/act-2025/act-tp/2025"
# Base DIR must be current folder
BASE_DIR="$(pwd)"

# Check if directory name is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <week_directory>"
    echo "Example: $0 week01"
    exit 1
fi

WEEK_DIR="$1"
WEEK_PATH="$BASE_DIR/$WEEK_DIR"

# Check if we're in the correct base directory
if [ "$(pwd)" != "$BASE_DIR" ]; then
    echo "Error: Please run this script from $BASE_DIR"
    echo "Current directory: $(pwd)"
    exit 1
fi

# Check if the specified week directory exists
if [ ! -d "$WEEK_PATH" ]; then
    echo "Error: Directory '$WEEK_PATH' not found!"
    echo "Available directories:"
    ls -d week*/ 2>/dev/null || echo "  (no week directories found)"
    exit 1
fi

# Function to modify conditionals in the LaTeX file
modify_conditionals() {
    local latex_file="$1"
    local show_solution="$2"
    local show_conseil="$3"
    
    # Use sed to replace the conditionals
    sed -i.tmp \
        -e "s/\\\\ShowSolutionfalse/\\\\ShowSolution${show_solution}/g" \
        -e "s/\\\\ShowSolutiontrue/\\\\ShowSolution${show_solution}/g" \
        -e "s/\\\\ShowConseilfalse/\\\\ShowConseil${show_conseil}/g" \
        -e "s/\\\\ShowConseiltrue/\\\\ShowConseil${show_conseil}/g" \
        "$latex_file"
    
    # Remove temporary file created by sed
    rm -f "${latex_file}.tmp"
}

# Function to compile PDF
compile_pdf() {
    local latex_file="$1"
    local output_name="$2"
    local week_path="$3"
    
    echo "  Compiling: $output_name"
    
    # Change to the week directory for compilation
    cd "$week_path"
    
    # Run pdflatex (run twice to ensure references are resolved)
    pdflatex -jobname="$output_name" "$(basename "$latex_file")" > /dev/null 2>&1
    pdflatex -jobname="$output_name" "$(basename "$latex_file")" > /dev/null 2>&1
    
    if [ $? -eq 0 ]; then
        echo "  ✓ Successfully generated: ${output_name}.pdf"
    else
        echo "  ✗ Error generating: ${output_name}.pdf"
        # Run again with output to show errors
        pdflatex -jobname="$output_name" "$(basename "$latex_file")"
    fi
    
    # Clean up auxiliary files
    rm -f "${output_name}.aux" "${output_name}.log" "${output_name}.out" "${output_name}.toc" "${output_name}.fls" "${output_name}.fdb_latexmk"
    
    # Return to base directory
    cd "$BASE_DIR"
}

# Function to process a single LaTeX file
process_latex_file() {
    local latex_file="$1"
    local week_path="$2"
    local base_name=$(basename "$latex_file" .tex)
    
    echo "Processing: $(basename "$latex_file")"
    
    # Create backup
    cp "$latex_file" "${latex_file}.backup"
    
    # Configuration 1: Both true
    echo "  Config 1: ShowSolution=true, ShowConseil=true"
    modify_conditionals "$latex_file" "true" "true"
    compile_pdf "$latex_file" "${base_name}_solution" "$week_path"
    
    # Configuration 2: Both false
    echo "  Config 2: ShowSolution=false, ShowConseil=false"
    modify_conditionals "$latex_file" "false" "false"
    compile_pdf "$latex_file" "${base_name}" "$week_path"
    
    # Configuration 3: ShowSolution=false, ShowConseil=true
    echo "  Config 3: ShowSolution=false, ShowConseil=true"
    modify_conditionals "$latex_file" "false" "true"
    compile_pdf "$latex_file" "${base_name}_conseil" "$week_path"
    
    # Restore original file
    mv "${latex_file}.backup" "$latex_file"
    echo "  ✓ Restored original file"
    echo
}

echo "Starting PDF generation for directory: $WEEK_DIR"
echo "Week path: $WEEK_PATH"
echo

# Find all .tex files that start with tp[single digit] in the specified week directory
tex_files_found=0
for tex_file in "$WEEK_PATH"/tp[0-9]*.tex; do
    if [ -f "$tex_file" ]; then
        tex_files_found=1
        process_latex_file "$tex_file" "$WEEK_PATH"
    fi
done

if [ $tex_files_found -eq 0 ]; then
    echo "No .tex files matching pattern 'tp[0-9]*.tex' found in $WEEK_DIR"
    echo
    echo "Available .tex files in $WEEK_DIR:"
    find "$WEEK_PATH" -name "*.tex" -exec basename {} \; 2>/dev/null | sed 's/^/  - /' || echo "  (none)"
else
    echo "========================================"
    echo "PDF generation completed for $WEEK_DIR!"
    echo "========================================"
    
    # Summary of generated files
    echo "Generated PDFs:"
    pdf_count=$(find "$WEEK_PATH" -name "*_solution.pdf" -o -name "*.pdf" -o -name "*_conseil.pdf" | wc -l)
    if [ $pdf_count -gt 0 ]; then
        find "$WEEK_PATH" -name "*_solution.pdf" -o -name "*.pdf" -o -name "*_conseil.pdf" -exec basename {} \; | sort | sed 's/^/  - /'
    else
        echo "  (no PDFs were generated)"
    fi
fi