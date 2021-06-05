## Created a package name loader
# Now create a class named Loader

import pandas as pd
import mysql.connector

class Loader:
    def __init__(self,file):
        global data
        data = pd.read_csv(file)
        data.fillna("None", inplace=True)
    #Required arguments are db_name and table_name
    def load(self,db_name,table_name,host="localhost",user="root",password=""):
        mydb = mysql.connector.connect(
            host = host,
            user = user,
            password = password
        )
        mycursor = mydb.cursor()

        #Creating Database
        mycursor.execute("CREATE DATABASE %s" % db_name)
        print("Database successfully created")
        mydb.close()

        #Creating table
        list_data = list(data.columns)
        list_datatype = list(data.dtypes)
        proper_datatype = []
        for value in list_datatype:
            if value == "object":
                proper_datatype.append("VARCHAR(500)")
            elif value == "int64":
                proper_datatype.append("INT")
            else:
                proper_datatype.append("NUMBER")

        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        mycursor = mydb.cursor()

        i = 0
        for i in range(len(list_data)):
            if i==0:
                mycursor.execute(f"CREATE TABLE {table_name} ( {list_data[i]} {proper_datatype[i]} )")
                i = i+1
            else:
                mycursor.execute(f"ALTER TABLE {table_name} ADD {list_data[i]} {proper_datatype[i]}")
                i = i+1
        print("Table successfully created")


        #Inserting Records
        data.fillna("None", inplace=True)

        for index, product in data.iterrows():
            sql = f"INSERT INTO {db_name}.{table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql, tuple(product))
        print("Records Inserted Successfully")
        mydb.commit()
        mydb.close()

        
