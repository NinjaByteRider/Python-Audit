import csv

with open("employee.csv", newline='') as f, open('admin_report.txt', 'w') as out:
    reader = csv.DictReader(f)
    for row in reader:
        if row["access_level"] == 'admin':
            out.write(row["name"] + "\n")
