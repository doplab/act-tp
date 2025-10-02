#!/bin/bash

# Script to remove files with extensions .log, .aux, and .out from a specified directory

# Check if directory argument is provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory>"
    echo "Example: $0 week01"
    exit 1
fi

# Get the directory name from the first argument
target_dir="$1"

# Check if the directory exists
if [ ! -d "$target_dir" ]; then
    echo "Error: Directory '$target_dir' does not exist in the current directory."
    exit 1
fi

# Extensions to remove including fls
extensions=("log" "aux" "out" "fdb_latexmk" "fls")

# Counter for removed files
removed_count=0

echo "Removing files with extensions .log, .aux, and .out from directory: $target_dir"

# Loop through each extension and remove matching files
for ext in "${extensions[@]}"; do
    # Find and remove files with current extension
    files_found=$(find "$target_dir" -maxdepth 1 -name "*.$ext" -type f)
    
    if [ -n "$files_found" ]; then
        echo "Removing *.$ext files:"
        find "$target_dir" -maxdepth 1 -name "*.$ext" -type f -print -delete
        removed_count=$((removed_count + $(echo "$files_found" | wc -l)))
    fi
done

echo "Cleanup complete. Removed $removed_count file(s)."