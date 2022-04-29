import psycopg2
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='alma45884'
)

current = config.cursor()

postgres_select_query = """select * from phonebook where username = %s"""
a=input('enter name that you wanna change: ')
current.execute(postgres_select_query,(a,))
postgres_update_query = """Update phonebook set number = %s where username = %s"""
b=input("enter number that you wanna change: ")
current.execute(postgres_update_query, (b, a))

config.commit()


current.close()
config.close()