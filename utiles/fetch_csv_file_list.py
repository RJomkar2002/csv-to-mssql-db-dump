from utiles.make_paths import make_paths
from os import listdir
def fetch_csv_file_list(file_endswith,input_file_dir,daily_file_dir):
    input_files_path=make_paths(input_file_dir,daily_file_dir)
    csv_file_list=[]
    csv_file_list_path=[]
    other_file_list=[]
    other_file_list_path=[]
    for file in listdir(input_files_path):
        if file.endswith(file_endswith):
            csv_file_list.append(file)
            csv_file_list_path.append(make_paths(input_files_path,file))
        else:
            other_file_list.append(file)
            other_file_list_path.append(make_paths(input_files_path,file))
    return csv_file_list_path,other_file_list_path,csv_file_list,other_file_list

