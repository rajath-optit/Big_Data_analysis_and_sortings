import pandas as pd

# Load the CSV file
df = pd.read_csv('sort_python_copy.csv', header=None)

# Insert a numbering column at the first position (index 0)
df.insert(0, 'Number', range(1, len(df) + 1))

# Save the updated DataFrame to a new CSV file
df.to_csv('numbered_sort_python.csv', index=False, header=False)

print(df)
