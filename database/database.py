import pymysql
from pymysql.cursors import DictCursor
from functools import cached_property
import private

""" 
THIS IS THE DATA PERSISTENCE LAYER
    This will handle the storage and retrieval of data form the database.
    A Persistence Layer contains components that facilitate the operation and 
    interaction with the database, such as:

    Data Access Objects (DAOs): For interacting with databases and 
        performing CRUD (Create, Read, Update, Delete) operations.
    Query Language: Allows the definition and execution of database queries to 
        retrieve and manipulate data.
    Caching Mechanism: In-memory caching of frequently accessed data to 
        optimize performance.
    Object-Relational Mapping (ORM) frameworks: Helps in mapping database records to 
        object-oriented models and simplifies database interactions.
"""


class Database:
    @cached_property
    def conn(self):
        print("Getting new connection...")
        return pymysql.connect(
                host='localhost',
                user='root',
                password=private.my_pass,
                database='coffee_shop_test',
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor)

    @property
    def curs(self) -> DictCursor:
        print("Creating cursor...")
        return self.conn.cursor()

    def fetchall(self, query: str) -> tuple:
        curs = self.curs
        curs.execute(query)
        print(f"Running {query}")
        return curs.fetchall()

    def fetchone(self, query: str) -> dict:
        curs = self.curs
        curs.execute(query)
        print(f"Running {query}")
        return curs.fetchone()

    def executemany(self, query: str, data: list[tuple]) -> None:
        print("Executing many...")
        self.curs.executemany(query, data)
        self.conn.commit()

    def execute(self, query: str, data: tuple) -> None:
        print("Executing one...")
        self.curs.execute(query, data)
        self.conn.commit()


db = Database()
