#To filter only admins
import csv

with open('employee.csv', newline = "") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['access_level'] == "admin":
            print(row["name"], "is admin")

