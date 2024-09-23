import os
import pandas as pd
from tabulate import tabulate

def generate_unique_filename(filename, extension):
    """
    Generates a unique filename by appending _1, _2, etc. if the file already exists.
    """
    base, ext = os.path.splitext(filename)
    if ext != extension:
        filename += extension
    
    counter = 1
    unique_filename = filename
    while os.path.exists(unique_filename):
        unique_filename = f"{base}_{counter}{extension}"
        counter += 1
    
    return unique_filename

def filter_checks_by_priority(file_path, priority):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Clean up whitespace in the relevant columns
    df['Control'] = df['Control'].str.strip()
    df['Category'] = df['Category'].str.strip()
    df[' priority '] = df[' priority '].str.strip()
    df['Mod'] = df['Mod'].str.strip()

    # Filter the DataFrame based on the selected priority
    filtered_df = df[df[' priority '] == f'p{priority}']

    # Print the output with the desired columns using tabulate for better formatting
    table_output = tabulate(filtered_df[['Category', 'Control', ' priority ', 'Mod']], headers='keys', tablefmt='pretty', showindex=False)
    print(table_output)

    # Ask if the user wants to save the output to a file
    save_file = input("Do you want to save the filtered with table results to a new file? (yes/no): ").strip().lower()

    if save_file == 'yes':
        # Get the file name for CSV, ensure extension is added and uniqueness
        csv_filename = input("Enter the name of the CSV file (e.g., 'filtered_output.csv'): ").strip()
        csv_filename = generate_unique_filename(csv_filename, '.csv')
        # Save CSV file
        filtered_df.to_csv(csv_filename, index=False)
        print(f"Filtered results have been saved to {csv_filename}")

        # Get the file name for the table format, ensure uniqueness
        table_filename = input("Enter the name of the table file (e.g., 'filtered_output.txt'): ").strip()
        table_filename = generate_unique_filename(table_filename, '.txt')
        # Save the table format to a file
        with open(table_filename, 'w') as f:
            f.write(table_output)
        print(f"Formatted table has been saved to {table_filename}")
    else:
        print("No file was saved.")

if __name__ == "__main__":
    # Specify the path to your CSV file
    file_path = 'converted_file.csv'

    # Get user input for priority level
    priority = input("Enter the priority level you want to filter by (1, 2, or 3): ")

    # Call the filtering function
    filter_checks_by_priority(file_path, priority)
