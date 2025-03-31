import shutil
import os
import datetime
def dump_processed_files(csv_file_list_path,csv_file_list, processed_file_dir_path):
    print('hi')
    i = 0
    for file1 in csv_file_list_path:
        print("hi")
        file2=file1.replace(csv_file_list[i],csv_file_list[i].split(".")[0]+"-"+f"{datetime.date.today()}_.csv")
        os.rename(file1,file2)
        # print(file1)
        shutil.move(file2, processed_file_dir_path)
        i += 1


def dump_other_files(other_file_list_path , other_file_dir_path):
    for file in other_file_list_path:
        shutil.move(file,other_file_dir_path)
        print(f"{file} is moved to other_files")

