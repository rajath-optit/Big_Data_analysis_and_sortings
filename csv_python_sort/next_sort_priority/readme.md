---

# README: Priority and File Conversion Python Programs

## Program 1: Convert Tab-Separated File to CSV

### Description:
This program allows users to convert a tab-separated file into a CSV format. The user provides the input file path, and the program checks if the file exists. If the file exists, it processes the content line by line, converts it into a CSV format, and saves the output to the user-specified file.

### Requirements:
- Python 3.x

### Installation:
No additional libraries are required beyond Python's standard library.

### Usage:
1. Run the program and input the path of the tab-separated file you want to convert.
2. You will be prompted to confirm if you want to convert the file to CSV format.
3. Provide the output filename with a `.csv` extension.

### Example:
```bash
python3 convert_csv_user_interface.py
```
#### Output:
```bash
Please enter the input file path: /path/to/checks.tsv
Do you want your file to get converted to CSV? (yes/no): yes
Please enter the output filename (with .csv extension): newfile.csv
Conversion to CSV completed.
```

---

## Program 2: Filter Checks by Priority

### Description:
This program reads a CSV file containing checks, cleans up whitespace in the relevant columns, and filters the checks based on a priority level (p1, p2, or p3). The filtered results are displayed in a formatted table using the `tabulate` library.

### Requirements:
- Python 3.x
- `pandas` library
- `tabulate` library

### Installation:
Install the required libraries by running:
```bash
pip install pandas tabulate
```

### Usage:
1. Run the program and provide the path to your CSV file and the priority level (1, 2, or 3) for filtering.
2. The program will output the filtered checks in a nicely formatted table.

### Example:
```bash
python3 filter_checks_by_priority.py
```
#### Output:
```bash
Enter the priority level you want to filter by (1, 2, or 3): 1
+------------------+-----------------------+------------+----------+
|     Category     |        Control         | priority   |   Mod    |
+------------------+-----------------------+------------+----------+
| Security         | AWS Root Account       | p1         | Enabled  |
| Network          | Public IP Exposure     | p1         | Enabled  |
+------------------+-----------------------+------------+----------+
```

---

## Program 3: Assign Priorities to Powerpipe Report

### Description:
This program reads priority control data from three separate CSV files (`priority1.csv`, `priority2.csv`, and `priority3.csv`), assigns the appropriate priority (p1, p2, or p3) to each control in a Powerpipe report, and saves the updated report with a new priority column.

### Requirements:
- Python 3.x
- `pandas` library

### Installation:
Install the required library by running:
```bash
pip install pandas
```

### Usage:
1. Place your priority CSV files and the Powerpipe report CSV file in the same directory.
2. Run the program to match controls in the Powerpipe report with the corresponding priority and save the updated report.

### Example:
```bash
python3 assign_priorities.py
```
#### Output:
```bash
Updated powerpipe report with priorities saved to powerpipe_report_with_priorities_updated.csv
```

---

This README file covers the functionality, setup, and usage of the three programs. Let me know if you need any adjustments!
