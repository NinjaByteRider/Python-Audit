import csv

with open("transactions.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["amount"]) > 10000 and row["country"] != "US":
            print(row)