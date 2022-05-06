import psycopg2
from config import database,user,password,host

def insert(connection, name, score):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO snake
            VALUES({name}, {score});"""
        )
    

def update(connection, name, score):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE snake
            SET user_score = {score}
            WHERE user_name = {name};"""
        )

connection = psycopg2.connect(
    database = database,
    user = user,
    host = host,
    password = password
    )


connection.autocommit = True

with connection.cursor() as cursor:
    cursor.execute(
        """select * from snake"""
    )
    select = cursor.fetchall()