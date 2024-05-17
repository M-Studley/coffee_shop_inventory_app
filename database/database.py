import pymysql
from pymysql.cursors import DictCursor
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
    conn: pymysql.Connection = None
    curs: DictCursor = None

    @classmethod
    def init(cls):
        Database.conn = pymysql.connect(
                host='localhost',
                user='root',
                password=private.my_pass,
                database='coffee_shop_test',
                charset='utf8mb4',
                cursorclass=DictCursor)
        Database.curs = Database.conn.cursor()

    @classmethod
    def fetchall(cls, query: str) -> tuple:
        Database.curs.execute(query)
        print(f"Running {query}")
        return Database.curs.fetchall()

    @classmethod
    def fetchone(cls, query: str) -> dict:
        Database.curs.execute(query)
        print(f"Running {query}")
        return Database.curs.fetchone()

    @classmethod
    def executemany(cls, query: str, data: list[tuple]) -> None:
        print("Executing many...")
        Database.curs.executemany(query, data)
        Database.conn.commit()

    @classmethod
    def execute(cls, query: str, data: tuple) -> None:
        print("Executing one...")
        Database.curs.execute(query, data)
        Database.conn.commit()


if not Database.conn:
    Database.init()
