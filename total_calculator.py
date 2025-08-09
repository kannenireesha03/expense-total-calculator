import csv

def calculate_total(file_name):
    total = 0
    with open(file_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    return total

# Change this to your CSV file name
file_name = "expenses.csv"
total_amount = calculate_total(file_name)
print(f"Total amount: {total_amount}")
