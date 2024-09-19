import csv

def sort_csv_by_priority(input_file, output_file):
    # Define the priority mapping
    priority_map = {"p1": 1, "p2": 2, "p3": 3}

    # Read the CSV data
    with open(input_file, mode='r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Extract header
        rows = list(reader)  # Extract all rows

    # Sort rows based on the 'priority' column (index 2) with the priority_map
    sorted_rows = sorted(rows, key=lambda row: priority_map.get(row[2].strip(), 99))

    # Write the sorted data to a new CSV file
    with open(output_file, mode='w', newline='') as sorted_csv:
        writer = csv.writer(sorted_csv)
        writer.writerow(header)  # Write header
        writer.writerows(sorted_rows)  # Write sorted rows

    print(f"CSV file '{input_file}' sorted by priority and saved to '{output_file}'.")

# Example usage
input_csv = 'your_input_file.csv'  # Replace with your actual input CSV file path
output_csv = 'sorted_output_file.csv'  # Replace with your desired output CSV file path
sort_csv_by_priority(input_csv, output_csv)
