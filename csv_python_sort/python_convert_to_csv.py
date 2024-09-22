import csv

# Input and output file paths
input_file = '/home/optit/Documents/Big_Data_analysis_and_sortings/csv_python_sort/checks.csv'  # Corrected filename
output_file = '/home/optit/Documents/Big_Data_analysis_and_sortings/csv_python_sort/converted_file.csv'

# Open the input file and process it line by line
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    csv_writer = csv.writer(outfile)

    for line in infile:
        # Split the line by tabs
        row = line.strip().split('\t')  # Split by tab character
        csv_writer.writerow(row)

print("Conversion to CSV completed.")
