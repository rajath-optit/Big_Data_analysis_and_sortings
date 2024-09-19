If you're working with an Excel sheet instead of a CSV file, you can use the `openpyxl` or `pandas` library in Python to read, sort, and display the data in the terminal. Here's a solution using `pandas`, which makes it easier to handle Excel files and manipulate the data:

### Python Script to Sort Excel Data by Priority and Print to Terminal

```python
import pandas as pd

def sort_excel_by_priority(input_file):
    # Read the Excel sheet into a pandas DataFrame
    df = pd.read_excel(input_file)

    # Define the priority mapping
    priority_map = {"p1": 1, "p2": 2, "p3": 3}

    # Replace priority values with the mapped numeric values
    df['priority_mapped'] = df['priority'].map(priority_map)

    # Sort the DataFrame by the mapped priority values
    df_sorted = df.sort_values('priority_mapped', na_position='last')

    # Drop the temporary mapped column
    df_sorted = df_sorted.drop(columns=['priority_mapped'])

    # Print the sorted DataFrame to the terminal
    print(df_sorted.to_string(index=False))

# Example usage
input_excel = 'your_input_file.xlsx'  # Replace with your actual Excel file path
sort_excel_by_priority(input_excel)
```

### Explanation:
1. **pandas Library**: The script uses `pandas` to handle Excel files.
2. **Sorting**: The `priority` column values (`p1`, `p2`, `p3`) are mapped to numeric values (`1`, `2`, `3`) to sort them in ascending order.
3. **Terminal Output**: The `to_string()` function is used to display the sorted DataFrame directly in the terminal.

### Install Required Library:
To install `pandas` and `openpyxl` (used to read Excel files), run:
```bash
pip install pandas openpyxl
```

### Expected Output in Terminal:

```plaintext
Category                                        Control priority                                     Importance of the check [COMMENT]        Mod Required not REquired
Account         Security contact information should be provided for an AWS account      p1                                                                 Compliance    YES        
ACM                   ACM certificates should have transparency logging enabled      p1                                                                 Compliance    YES        
API Gateway                API Gateway methods authorizer should be configured      p1                                                                 Compliance               
AppSync                         AppSync graphql API logging should be enabled      p1 Enabling AppSync GraphQL API logging is crucial for security as it helps monitor, audit Compliance               
Account                      AWS account should be part of AWS Organizations      p3                                                                 Compliance               
API Gateway    Access logging should be configured for API Gateway V2 Stages      p3                                                                 Compliance               
```

This script will read the Excel file, sort the rows based on the priority column, and print the sorted result directly in your terminal.
