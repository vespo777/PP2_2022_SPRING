import psycopg2
from config import host,database,user,password
import csv

def create(connection):
    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE PhoneBook
            (
                user_first_name varchar(30) NOT NULL,
                user_last_name varchar(30) NOT NULL,
                user_phone varchar(30)
            );"""
        )

def insert_terminal(connection, first_name, last_name, phone):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO PhoneBook(user_first_name, user_last_name, user_phone)
            VALUES('{first_name}','{last_name}','{phone}');"""
        )

def insert_csv(connection):
    with open('dates.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            with connection.cursor() as cursor:
                cursor.execute(
                f"""INSERT INTO PhoneBook(user_first_name, user_last_name, user_phone)
                VALUES({line[0]},{line[1]},{line[2]});"""
        )

def update_first_name(connection, first_name, phone):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE PhoneBook
                SET user_first_name = {first_name}
                WHERE user_phone = {phone};"""
        )

def update_phone(connection, first_name, phone):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE PhoneBook
                SET user_phone = {phone}
                WHERE user_first_name = {first_name};"""
        )

def delete(connection, phone):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""DELETE FROM PhoneBook
            WHERE user_phone = {phone};"""
        )

def main():

    try:
        connection = psycopg2.connect(
            host = host,
            database = database,
            user = user,
            password = password
        )

        connection.autocommit = True
        # create(connection)
        # first_name = input()
        # last_name = input()
        phone = input()
        # insert_terminal(connection, first_name, last_name, phone)
        delete(connection, phone)
    except Exception as ex:
        print(ex)

    finally:
        if connection:
            connection.close()
            print('connection is closed')

if __name__=='__main__':
    main()