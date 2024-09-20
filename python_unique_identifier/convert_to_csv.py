import pandas as pd

# Load the copied Excel file
file_path = 'sort_python_copy.xlsx'
df = pd.read_excel(file_path)

# Save it as a CSV file
df.to_csv('sort_python.csv', index=False)
print("Excel file successfully converted to CSV.")
