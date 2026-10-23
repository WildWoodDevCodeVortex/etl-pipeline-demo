
import csv


def extract_data():
    input_file = "data/input.csv"
    rows = []

    with open(input_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows
