
import psycopg2
from config import config

def connect():
    conn = None
    try:
        # read parameters
        params = config()

        # connect to the server
        print('Connecting to the database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute('SELECT version()')

        # fetch and print
        db_ver = cur.fetchone()
        print('Database version: {ver}'.format(ver = db_ver))

        # close the comms
        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()

else:
    print('main executed externally.')

