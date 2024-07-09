import requests
import mysql.connector
from models.database import Database
from sqlConfig import MYSQL_USER, MYSQL_DATABASE, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT
from models.schemas import User


def get_db():
    db = Mysql_database()
    return db


class Mysql_database(Database):
    def __init__(self):
        self.config = {
            'user': f"{MYSQL_USER}",
            'password': f"{MYSQL_PASSWORD}",
            'host': f"{MYSQL_HOST}",
            'port': MYSQL_PORT,
            'database': f"{MYSQL_DATABASE}"
        }
        self.connetion = self.connect()

    def connect(self):
        mydb = mysql.connector.connect(**self.config)
        return mydb

    def __execute_query(self, query, commit=False):
        mydb = self.connect()
        cursor = mydb.cursor()
        cursor.execute(query)
        if commit:
            mydb.commit()
        return cursor.fetchall()

    def get_user_by_username(self, username: str):
        query = f"SELECT * FROM User WHERE username = '{username}'"
        return self.__execute_query(query)

    def add_user_to_db(self, user: User):
        query = f"""INSERT INTO User (username, password_hash, email, role) VALUES ('{user.username}', '{user.password}','{user.email}', '{user.role}');"""
        print(query)
        self.__execute_query(query, commit=True)
