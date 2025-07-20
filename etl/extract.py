import csv

file_path = "/Users/sylwia/Documents/my-reps/sylwias-mini-project/Cafe.csv"

def extract_data(filepath = file_path):
    data = []
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

print(extract_data())