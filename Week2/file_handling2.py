import csv

def csv_to_dict(csv_file):
    data_dict = {}
    with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if len(row) >= 2:
                key, value = row[0], row[1]
                data_dict[key] = value
    return data_dict

if __name__ == "__main__":
    csv_file_name = "c:/Users/davit/Documents/Kreavistorm/week2/Nueva carpeta/Catalog.csv"  
    data_dict = csv_to_dict(csv_file_name)

    if data_dict:
        print("Dictionary created from CSV:")
        for key, value in data_dict.items():
            print(f"{key}: {value}")
    else:
        print(f"Unable to create a dictionary from '{csv_file_name}'.")
