def dump_into_db_acc_schema(cur_of_mssql,schema_and_table_name,all_csv_data_list):
    for data in all_csv_data_list:
        sql_insert_querry=f"insert into {schema_and_table_name} values {tuple(data.values())}"
        cur_of_mssql.execute(sql_insert_querry)
        cur_of_mssql.commit()
    print("Data inserted sucessfully!!!")
