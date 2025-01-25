#!/bin/bash

# Define the output file
output_md="combined_readme.md"

# Loop through Experiment1 to Experiment12 and concatenate README.md files
for i in {1..12}
do
  experiment_dir="Experiment$i"
  readme_file="$experiment_dir/README.md"
  
  if [ -f $readme_file ]; then
    echo "Processing $readme_file"
    echo "" >> $output_md
    cat $readme_file >> $output_md
    echo -e "\n\n" >> $output_md # Add some space between files
  else
    echo "README.md not found in $experiment_dir"
  fi
done

echo "Markdown file generated: $output_md"
