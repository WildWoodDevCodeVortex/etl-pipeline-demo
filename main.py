
from ETL.extract import extract_data
from ETL.transform import transform_data
from ETL.load import load_data


def main():
    raw_data = extract_data()
    transformed_data = transform_data(raw_data)
    output_file = load_data(transformed_data)

    print("ETL pipeline completed successfully.")
    print(f"Output saved to {output_file}")


if __name__ == "__main__":
    main()
