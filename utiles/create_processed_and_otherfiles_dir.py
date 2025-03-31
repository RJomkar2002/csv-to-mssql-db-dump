from utiles.make_paths import make_paths
from os import mkdir
from os.path import exists

def create_processed_and_otherfiles_dirs():
    processed_file_path = make_paths("input","processed_files")
    other_file_path = make_paths("input","other_files")

    processed_file_exists = not exists(processed_file_path)
    other_file_exists = not exists(other_file_path)

    if processed_file_exists:
        mkdir(processed_file_path)
        print("processed file created!!!")

    if other_file_exists:
        mkdir(other_file_path)
        print("other file created!!!")
    return processed_file_path , other_file_path

