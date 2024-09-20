import pandas as pd

# Load your Excel file without headers
df = pd.read_excel('sort_python.xlsx', header=None)

# Print the DataFrame for debugging
print("Data in the DataFrame:")
print(df)

# Extract columns as lists and strip whitespace
column_a = df[0].dropna().tolist()
column_b = df[1].dropna().tolist()

# Strip whitespace from items
column_a = [item.strip() for item in column_a]
column_b = [item.strip() for item in column_b]

# Convert both lists to sets
set_a = set(column_a)
set_b = set(column_b)

# Find repeated items (intersection of both sets)
repeated_items = set_a.intersection(set_b)

# Find unique items (items that are in either A or B, but not both)
unique_items = (set_a.union(set_b)) - repeated_items

# Debug: Print unique items
print("Unique Items:", unique_items)

# Output the unique, non-repeated items
print("Unique Non-Repeated Elements from both columns:")
for item in sorted(unique_items):
    print(item)
