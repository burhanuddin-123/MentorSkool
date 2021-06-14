# Importing Differnt modules
###########################################################

from pandas.errors import ParserError
import pandas as pd
import mysql.connector
import sys

class Loader:
## Initialization of code that is Constructor
    def __init__(self,file):
        try:
            self.data = pd.read_csv(file)
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

## Establishing Connection
###########################################################

    def get_cursor(self,host,user,password):
        try:
            self.mydb =  mysql.connector.connect(
                host=host,
                user=user,
                password=password,
            )
            #
            cursor = self.mydb.cursor()
            return cursor
        except mysql.connector.Error as err:
            print(err)
            return None

## Creating database
###########################################################

    def create_database(self,cursor,db_name):
        try:
            cursor.execute(f"CREATE DATABASE {db_name}")
            return True
        except mysql.connector.Error as err:
            print(err.msg)
            return None
            # mydb.close()

## Creating Table
###########################################################

    def create_table(self,cursor,db_name,table_name):
        self.list_data = list(self.data.columns)
        list_datatype = list(self.data.dtypes)
        self.proper_datatype = []
        for value in list_datatype:
            if value == "object":
                self.proper_datatype.append("VARCHAR(500)")
            elif value == "int64":
                self.proper_datatype.append("INT")
            else:
                self.proper_datatype.append("NUMBER")

        # try:
        #     self.mydb = self.get_cursor(host, user, password,db_name)
        # except mysql.connector.Error:
        #     print("Connection can't be established. Check whether the Sql server is on or not")
        #     return
        # else:
        #     self.cursor = self.mydb.cursor()

        try:
            cursor.execute(f"CREATE TABLE {db_name}.{table_name} ( {self.list_data[0]} {self.proper_datatype[0]} ) ")
            return True
        except mysql.connector.Error as err:
            print("Can't Create Table :-",err.msg)
            return None

## Altering Table
###########################################################

    def alter_table(self,cursor,db_name,table_name):
        try:
            for i in range(1,len(self.list_data)):
                cursor.execute(f"ALTER TABLE {db_name}.{table_name} ADD {self.list_data[i]} {self.proper_datatype[i]}")
            return True
        except mysql.connector.Error:
            print(f"Can't Alter Table '{table_name}'")
            return None

## Load the csv file data to sql table
###########################################################

    def load_data_in(self,cursor,db_name,table_name):
        self.data.fillna("None", inplace=True)
        try:
            for index, product in self.data.iterrows():
                # sql = f"INSERT INTO {table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                ##Dynamic query
                cursor.execute(f"INSERT INTO {db_name}.{table_name} VALUES {tuple(product)} ")

                ### Another way
                # str_s = ','.join(['%s'] * len(self.list_data))
                # sql = '''INSERT INTO %s.%s VALUES (%s) ''' % (db_name,table_name,str_s)
                # self.cursor.execute(sql,tuple(product))
            return True
        except mysql.connector.Error as err:
            print(err)
            return None

## Function Calls
###########################################################

    def load(self,db_name,table_name,host="localhost",user="root",password=""):
        cursor = self.get_cursor(host,user,password)
        if not cursor:
            print("Connection Failed")
            return

        status = self.create_database(cursor,db_name)
        if not status:
            print("Database Creation Failed")
            return
        print("Database Created Successfully")

        status = self.create_table(cursor,db_name,table_name)
        if not status:
            print("Table Creation Failed")
            return
        else:
            status = self.alter_table(cursor,db_name,table_name)
            if not status:
                print("Table is not properly created")
                return
        print("Table Created Successfully")

        # self.alter_table(db_name,table_name)
        status = self.load_data_in(cursor,db_name,table_name)
        if not status:
            print("Records Can't be loaded")
            return
        print("Records Inserted Successfully")
        self.mydb.commit() # After inserting records we are committing it or saving it permanently in database
        self.mydb.close() # Closing the connection