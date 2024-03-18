"""
CREDIT TO https://thinkingneuron.com/reading-data-from-mysql-database-in-python/
"""

from sqlalchemy import create_engine
import mysql.connector as sql
import MySQLdb
import pandas as pd

class SQLLink:
    def __init__(self):
        
        self._connection = 'localhost'
        self._username = 'root'
        self._password = 'SQL-PasswordA'
        self._database_name = 'MySQL'

    def get_data(self):
        
        # Creating the database connection
        #db_connection_str = "mysql+pymysql://" + self._username + ":" + self._password + '@' + self._connection + '/' + self._database_name
        #db_connection = create_engine(db_connection_str)
        
        # Employees table must be present in the database
        #DataFromDB = pd.read_sql('SELECT * FROM chatbot.queries', con = db_connection)
        return pd.Dataframe()

    def add_data(self, question):
        database = MySQLdb.connect(host = self._connection, user = self._username, password = self._password, db = self._database_name)
        current = database.cursor()
        line = 'INSERT INTO chatbot.new_questions (question_column) VALUES ' + '(\'' + question + '\')' + ';'
        current.execute(line)
        database.commit()
        database.close()
        
        
        







