from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data_to_mysql

def main():
    while True:
        print("\n--- Cafe ETL Menu ---")
        print("1. Extract Data")
        print("2. Transform Data")
        print("3. Load Data to MySQL")
        print("4. Run Full ETL")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            data = extract_data("Cafe.csv")
            print(f"✅ Extracted {len(data)} records.")
        elif choice == "2":
            data = extract_data("Cafe.csv")
            cleaned = transform_data(data)
            print(f"✅ Transformed. {len(cleaned)} records ready for loading.")
        elif choice == "3":
            data = extract_data("Cafe.csv")
            cleaned = transform_data(data)
            load_data_to_mysql(cleaned)
        elif choice == "4":
            data = extract_data("Cafe.csv")
            cleaned = transform_data(data)
            load_data_to_mysql(cleaned)
        elif choice == "5":
            break
        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
