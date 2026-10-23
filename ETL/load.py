
import json


def load_data(transformed_data):
    output_file = "data/output.json"

    with open(output_file, mode="w", encoding="utf-8") as file:
        json.dump(transformed_data, file, indent=4)

    return output_file
