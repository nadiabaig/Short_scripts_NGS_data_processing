

#!/bin/bash

# Set the input directory
input_dir=/1data/Nadia/splitted_bams

# Set the output directory
output_dir=/1data/Nadia/splitted_bams/250kb

# Set the chunk size in bytes
chunk_size=$((350 * 1000))

# Loop over all BAM files in the input directory
for bam_file in "$input_dir"/*.bam; do
  # Get the base filename without extension
  base_filename=$(basename "$bam_file" .bam)

  # Get the size of the BAM file
  file_size=$(stat -c%s "$bam_file")

  # Calculate the number of chunks to split the BAM file into
  num_chunks=$(( ($file_size + $chunk_size - 1) / $chunk_size ))

  # Split the BAM file into multiple BAM files of 350kb
  for ((i=1; i<=$num_chunks; i++)); do
    start=$((($i-1)*$chunk_size))
    end=$((($i*$chunk_size)-1))
    samtools view -hb "$bam_file" "$start"-"$end" > "$output_dir/$base_filename.chunk$i.bam"
  done
done

