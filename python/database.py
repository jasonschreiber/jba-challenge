import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, conn_path):
        self.conn_path = conn_path
        self.table_name = 'precipitation'
        self.conn = None

        self.initialise()

    def initialise(self):
        """
        Initialise connection to sqlite database. create database and tables if they don't
        exist or just create connection if the database exists.
        :return:
        """
        self.create_connection()
        self.create_table()

    def create_connection(self):
        """
        Create a database connection to a SQLite database. Will create a database if it does not exist
        or will connect to the existing database
        :return:
        """
        try:
            self.conn = sqlite3.connect(self.conn_path)
            print(sqlite3.version)
        except Error as e:
            print(e)

    def close_connection(self):
        """
        Close database connection
        :return:
        """
        self.conn.close()

    def create_table(self):
        """
        Create table and fields for "precipitation" values
        :return:
        """

        sql_create_table = f"""
                            CREATE TABLE IF NOT EXISTS {self.table_name} (
                                id integer PRIMARY KEY,
                                Xref integer NOT NULL,
                                Yref integer NOT NULL,
                                Date text NOT NULL,
                                Value integer NOT NULL
                            );
                           """
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql_create_table)
        except Error as e:
            print(e)
        finally:
            del cursor

    def insert_many_rows(self, rows):
        """
        Uses executemany function to insert batch of data rows into the connected database
        :param rows:
        :return:
        """
        sql_insert = f"INSERT INTO {self.table_name}(Xref, Yref, Date, Value) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        try:

            cursor.executemany(sql_insert, rows)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            del cursor

    def truncate_table(self):
        """
        Truncate table for cleanup
        :return:
        """
        sql_truncate = f'DELETE FROM {self.table_name};'

        try:
            cursor = self.conn.cursor()
            cursor.execute(sql_truncate)
            self.conn.commit()
        except Error as e:
            print(e)
        finally:
            del cursor


if __name__ == '__main__':
    database = Database(r'db\pythonsqlite.db')
    #database.create_connection()
    database.truncate_table()
