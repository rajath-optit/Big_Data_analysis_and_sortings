import pandas as pd
from tabulate import tabulate

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
    print(tabulate(filtered_df[['Category', 'Control', ' priority ', 'Mod']], headers='keys', tablefmt='pretty', showindex=False))

if __name__ == "__main__":
    # Specify the path to your CSV file
    file_path = 'converted_file.csv'

    # Get user input for priority level
    priority = input("Enter the priority level you want to filter by (1, 2, or 3): ")

    # Call the filtering function
    filter_checks_by_priority(file_path, priority)
