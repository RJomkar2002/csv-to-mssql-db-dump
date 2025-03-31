import csv
def read_csv_files(csv_file_list_path):
    all_csv_data_list = []
    for csv_path in csv_file_list_path:
        with open(csv_path)as fp:
            data=list(csv.DictReader(fp))
            all_csv_data_list.extend(data)
    print("CSV files readed")
    return all_csv_data_list



