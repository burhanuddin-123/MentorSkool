## Importing Differnt modules
###########################################################

from pandas.errors import ParserError
import pandas as pd
import mysql.connector
import sys


class Loader:
    ## Initialization of code that is Constructor
    def __init__(self, file):
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

    def get_cursor(self, host, user, password, database=""):

        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    ## Creating database
    ###########################################################

    def create_database(self, host, user, password, db_name):
        try:
            self.mydb = self.get_cursor(host, user, password)
        except mysql.connector.Error:
            print("Connection can't be established. Check whether the Sql server is on or not")
            return
        else:
            self.cursor = self.mydb.cursor()
            try:
                self.cursor.execute(f"CREATE DATABASE {db_name}")
            except mysql.connector.Error as err:
                print(err.msg)
            else:
                print("Database successfully created")
                # mydb.close()

    ## Creating Table
    ###########################################################

    def create_table(self, db_name, table_name):

        ## Fetching columns and its datatype from csv file
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

        ## Creating table after fetching columns from csv
        try:
            self.cursor.execute(f"CREATE TABLE {db_name}.{table_name} ( {self.list_data[0]} {self.proper_datatype[0]} ) ")
        except mysql.connector.Error as err:
            print("Can't Create Table :-", err.msg)
            return
        else:
            print(f"Table {table_name} succesfully created")

    ## Altering Table
    ###########################################################

    def alter_table(self, db_name, table_name):
        try:
            for i in range(1, len(self.list_data)):
                self.cursor.execute(
                    f"ALTER TABLE {db_name}.{table_name} ADD {self.list_data[i]} {self.proper_datatype[i]}")
        except mysql.connector.Error:
            print(f"Can't Alter Table '{table_name}'")
            return
        else:
            print(f"Table {table_name} succesfully Altered")

    ## Load the csv file data to sql table
    ###########################################################

    def load_data_in(self, db_name, table_name):
        self.data.fillna("None", inplace=True)
        try:
            for index, product in self.data.iterrows():
                # sql = f"INSERT INTO {table_name} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                ##Dynamic query
                self.cursor.execute(f"INSERT INTO {db_name}.{table_name} VALUES {tuple(product)} ")

                # Another way
                # str_s = ','.join(['%s'] * len(self.list_data))
                # sql = '''INSERT INTO %s.%s VALUES (%s) ''' % (db_name,table_name,str_s)
                # self.cursor.execute(sql,tuple(product))

        except mysql.connector.Error as err:
            print(err)
        else:
            print("Records Inserted Successfully")
        self.mydb.commit()
        self.mydb.close()

    ## Function Calls
    ###########################################################

    def load(self, db_name, table_name, host="localhost", user="root", password=""):
        self.create_database(host, user, password, db_name)
        self.create_table(db_name, table_name)
        self.alter_table(db_name, table_name)
        self.load_data_in(db_name, table_name)