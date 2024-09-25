import pandas as pd

# Step 1: Load the CSV files
no_priority_file = 'no_priorirty_added.csv'
with_priority_file = 'with_priority.csv'

# Step 2: Read both files into DataFrames
no_priority_df = pd.read_csv(no_priority_file)
with_priority_df = pd.read_csv(with_priority_file)

# Step 3: Create a dictionary from the with_priority.csv file mapping Control_id to priority
priority_dict = with_priority_df.set_index('Control_id')[' priority '].to_dict()

# Step 4: Create a function to assign priorities based on Control_id
def assign_priority(control_id):
    return priority_dict.get(control_id, 'No Priority')  # Default to 'No Priority' if not found

# Step 5: Apply the function to add a priority column to the no_priority_df DataFrame
no_priority_df['priority'] = no_priority_df['Control_id'].apply(assign_priority)

# Step 6: Save the updated DataFrame with priorities to a new CSV file
output_file = 'no_priority_added_with_priorities.csv'
no_priority_df.to_csv(output_file, index=False)

print(f"Updated file saved as {output_file}")
