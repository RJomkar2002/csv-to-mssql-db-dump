from utiles.fetch_csv_file_list import fetch_csv_file_list
from utiles.read_csv_files import read_csv_files
from utiles.mssql_db_conn import db_conn_mssql
from business_logic.dump_into_db_acc_schema import dump_into_db_acc_schema
from utiles.dump_processed_and_other_files import dump_other_files
from utiles.dump_processed_and_other_files import dump_processed_files
from utiles.create_processed_and_otherfiles_dir import create_processed_and_otherfiles_dirs

def main():

    #fetch csv file and other file's list in the input data
    file_endswith=".csv"
    input_file_dir="input"
    daily_file_dir='daily_files'
    csv_file_list_path , other_file_list_path ,csv_file_list , other_file_list = fetch_csv_file_list(file_endswith,input_file_dir,daily_file_dir)

    #read csv file.
    all_csv_data_list = read_csv_files(csv_file_list_path)#pass csv_files_path

    #connect_to_database.
    db_name=input("Enter database name: ").strip()
    cur_of_mssql , conn_of_mssql = db_conn_mssql(db_name)

    #dump all csv data in given schema.table
    schema_and_table_name=input("Enter schema name : ").strip()+"."+input("Enter table name : ").strip()#shema.table

    dump_into_db_acc_schema(cur_of_mssql,schema_and_table_name,all_csv_data_list)
    conn_of_mssql.close()
    print(f"{db_name} DB closed successfully...")

    processed_file_dir_path , other_file_dir_path = create_processed_and_otherfiles_dirs()
    print(processed_file_dir_path)
    print(other_file_dir_path)
    dump_other_files(other_file_list_path , other_file_dir_path)
    dump_processed_files(csv_file_list_path , csv_file_list , processed_file_dir_path)

if __name__=="__main__":
    main()
