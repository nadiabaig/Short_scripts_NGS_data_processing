#!/bin/bash

# Set the input and output directories
input_dir=/path/to/input/files
output_dir=/path/to/output/files

# Set the adapter sequence (Note this one is for single end data)
adapter_sequence=AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC  #change this with your adapter sequence

# Loop over all fastq files in the input directory
for fastq_file in "$input_dir"/*.fastq.gz; do
  # Get the base filename without extension
  base_filename=$(basename "$fastq_file" .fastq.gz)

  # Run cutadapt
  cutadapt \
    -a "$adapter_sequence" \
    -o "$output_dir/$base_filename.trimmed.fastq.gz" \
    "$fastq_file" \
    > "$output_dir/$base_filename.cutadapt.log" \
    2>&1
done

############# for paired end data##############
#!/bin/bash

# Set the input and output directories
input_dir=/path/to/input/files
output_dir=/path/to/output/files

# Set the adapter sequences for both the forward and reverse reads
adapter_fwd=AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC
adapter_rev=AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT

# Loop over all fastq files in the input directory
for fastq_file in "$input_dir"/*_R1.fastq.gz; do
  # Get the base filename without extension
  base_filename=$(basename "$fastq_file" _R1.fastq.gz)

  # Define the input and output file names for both forward and reverse reads
  input_fwd="$input_dir/$base_filename"_R1.fastq.gz
  input_rev="$input_dir/$base_filename"_R2.fastq.gz
  output_fwd="$output_dir/$base_filename"_R1.trimmed.fastq.gz
  output_rev="$output_dir/$base_filename"_R2.trimmed.fastq.gz

  # Run cutadapt on both the forward and reverse reads
  cutadapt \
    -a "$adapter_fwd" \
    -A "$adapter_rev" \
    -o "$output_fwd" \
    -p "$output_rev" \
    "$input_fwd" \
    "$input_rev" \
    > "$output_dir/$base_filename.cutadapt.log" \
    2>&1
done

