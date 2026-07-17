import pyodbc
import pandas as pd
from config import Config


class Database:

    def __init__(self):

        self.connection_string = (
            f"DRIVER={{{Config.DRIVER}}};"
            f"SERVER={Config.SERVER};"
            f"DATABASE={Config.DATABASE};"
            f"Trusted_Connection={Config.TRUSTED_CONNECTION};"
        )

    def connect(self):

        try:

            connection = pyodbc.connect(self.connection_string)

            print("Connected to SQL Server Successfully")

            return connection

        except Exception as e:

            print("Connection Failed")

            print(e)

            return None

    def execute_query(self, query):

        connection = self.connect()

        dataframe = pd.read_sql(query, connection)

        connection.close()

        return dataframe