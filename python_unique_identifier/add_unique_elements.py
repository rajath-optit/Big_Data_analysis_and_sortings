import pandas as pd

# Load the CSV file
df = pd.read_csv('numbered_sort_python.csv', header=None)

# Combine the unique elements from both columns
unique_a = set(df[0])  # Column A
unique_b = set(df[1])  # Column B

# Find non-repeated elements
non_repeated_a = unique_a - unique_b  # Elements in A that are not in B
non_repeated_b = unique_b - unique_a  # Elements in B that are not in A

# Combine the results into a single DataFrame
result = pd.DataFrame(list(non_repeated_a.union(non_repeated_b)), columns=['Unique Elements'])

# Save the results to a new CSV file
result.to_csv('unique_elements.csv', index=False)

print("Unique non-repeated elements saved to 'unique_elements.csv'")
