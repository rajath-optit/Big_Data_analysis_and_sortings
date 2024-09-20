import pandas as pd

# Load the Excel file
file_path = 'sort_python.xlsx'  # Adjust the file name if you saved it with a different name
df = pd.read_excel(file_path, header=None)

# Display the data for debugging
print("Data in the DataFrame:")
print(df)

# Extract the columns
column_a = df[0].dropna().tolist()  # First column (index 0)
column_b = df[1].dropna().tolist()  # Second column (index 1)

# Convert both lists to sets
set_a = set(column_a)
set_b = set(column_b)

# Find repeated items (intersection of both sets)
repeated_items = set_a.intersection(set_b)

# Find unique items (items that are in either A or B, but not both)
unique_items = (set_a.union(set_b)) - repeated_items

# Output the unique, non-repeated items
print("\nUnique Non-Repeated Elements from both columns:")
for item in sorted(unique_items):
    print(item)
