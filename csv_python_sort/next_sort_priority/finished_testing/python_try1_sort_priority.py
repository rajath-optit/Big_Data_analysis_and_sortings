import pandas as pd

def filter_checks_by_priority(file_path, priority):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Filter the DataFrame based on the selected priority
    filtered_df = df[df[' priority '].str.strip() == f'p{priority}']

    # Print the output with the desired columns
    print(filtered_df[['Category', 'Control', ' priority ', 'Mod']].to_string(index=False))

if __name__ == "__main__":
    # Specify the path to your CSV file
    file_path = 'converted_file.csv'  # Updated to the correct file

    # Get user input for priority level
    priority = input("Enter the priority level you want to filter by (1, 2, or 3): ")

    # Call the filtering function
    filter_checks_by_priority(file_path, priority)
