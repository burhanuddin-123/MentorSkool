## Created a package name loader
# Now create a class named Loader

import pandas as pd
import mysql.connector

class Loader:
    def __init__(self,file):
        global data
        try:
            data = pd.read_csv(file)
            data.fillna("None", inplace=True)
        except FileNotFoundError as fer:
            print(fer.filename, ":-", fer.strerror)
        except IOError as ier:
            print("Input Error", ier)
        except PermissionError as per:
            print("Permission Error", per)
        except ParserError as par:
            print(f"{file} type is Incorrect as appropriate type should be '.csv' or {file} is corrupted")
        except Exception:
            print(sys.exc_info())
    #Required arguments are db_name and table_name
    def load(self,db_name,table_name,host="localhost",user="root",password=""):
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password
            )
        except mysql.connector.Error as err:
            # print(err.msg)
            # print(err)
            print("Connection can't be established. Check whether the Sql server is on or not")
            return
        else:
            mycursor = mydb.cursor()

        #Creating Database
        try:
            mycursor.execute("CREATE DATABASE %s" % db_name)
        except mysql.connector.Error as err:
            print(err.msg)
        else:
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

        try:
            for i in range(len(list_data)):
                if i == 0:
                    mycursor.execute(f"CREATE TABLE {table_name} ( {list_data[i]} {proper_datatype[i]} )")
                    i = i + 1
                else:
                    mycursor.execute(f"ALTER TABLE {table_name} ADD {list_data[i]} {proper_datatype[i]}")
                    i = i + 1
        except mysql.connector.Error as err:
            print(err.msg)
        else:
            print("Table successfully created")


        #Inserting Records
        data.fillna("None", inplace=True)
        try:
            for index, product in data.iterrows():
                sql = f"INSERT INTO {db_name}.{table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(sql, tuple(product))
        except mysql.connector.Error as err:
            print(err)
        else:
            print("Records Inserted Successfully")
        mydb.commit()
        mydb.close()

        
