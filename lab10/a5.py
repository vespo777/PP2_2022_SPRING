import psycopg2
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='alma45884'
)

current = config.cursor()

postgres_delete_query = """Delete from phonebook where username = %s"""
a=input('enter name that you wanna delete: ')
current.execute(postgres_delete_query,(a,))
config.commit()

current.close()
config.close()