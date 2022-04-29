import psycopg2
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='alma45884'
)

current = config.cursor()

postgres_insert_query=''' INSERT INTO phonebook (username,number) VALUES (%s,%s)'''
a=input('enter your name: ')
b=input("enter your number: ")
current.execute(postgres_insert_query,(a,b))
config.commit()

current.close()
config.close()