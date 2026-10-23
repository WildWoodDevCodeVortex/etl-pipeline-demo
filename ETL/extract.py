
import csv
# Feature update 1: Read source CSV records.
# Feature update 2: Preserve the CSV column names.
def extract_data():
    input_file = "data/input.csv"
    rows = []

    with open(input_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows
