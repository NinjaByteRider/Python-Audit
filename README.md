# Python CSV Audit Practice

## Overview
This project demonstrates how Python can be used to analyze CSV data for basic audit and compliance testing.

The scripts simulate common audit procedures such as:
- Reviewing employee access levels
- Identifying privileged users
- Detecting high-value transactions
- Applying simple fraud detection logic



## Skills Used
- Python
- CSV file handling
- Conditional logic
- Loops
- Data filtering
- Basic audit analytics



## Project Files

### CSV Data Files
- `employee.csv`
- `transactions.csv`

### Python Scripts
- `read_and write_text_files.py`
- `filter_admin.py`
- `write_report.py`
- `transactions_filter.py`
- `fraud_logic.py`



## Example Audit Logic

### Filter admin users
```python
if row["access_level"] == "admin":
print(row["name"])
