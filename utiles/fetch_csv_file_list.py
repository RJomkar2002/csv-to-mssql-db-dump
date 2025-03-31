import os
def fetch_csv_file_list(file_endswith,input_file_dir):
    input_files_path=os.path.join(os.getcwd(),input_file_dir)
    csv_file_list=[]
    csv_file_list_path=[]
    other_file_list=[]
    for file in os.listdir(input_files_path):
        if file.endswith(file_endswith):
            csv_file_list.append(file)
            csv_file_list_path.append(os.path.join(input_files_path,file))
        else:
            other_file_list.append(file)
    return csv_file_list_path,csv_file_list,other_file_list

