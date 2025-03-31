import pyodbc
import os
def db_conn_mssql(mssql_db_name):
    DRIVER=os.getenv("DRIVER")
    SERVER=os.getenv("SERVER")
    Trusted_Connection=os.getenv("Trusted_Connection")

    connstr = f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={mssql_db_name};Trusted_Connection={Trusted_Connection}'
    conn_of_mssql=pyodbc.connect(connstr)
    cur_of_mssql=conn_of_mssql.cursor()
    print(f"MsSQL {mssql_db_name} DB connected successfully...")
    return cur_of_mssql,conn_of_mssql
