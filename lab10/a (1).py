import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    port = '5432',
    user='postgres',
    password='alma45884'
)

current = config.cursor()
current.execute(
    '''
    CREATE TABLE phonebook(
        username VARCHAR(20),
        number VARCHAR(12)
    )
    '''
)
config.commit()

current.close()
config.close()