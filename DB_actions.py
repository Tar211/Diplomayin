import mysql.connector
from mysql.connector import Error


def connect():
    try:

        conn = mysql.connector.connect(host = 'localhost', database = 'mysql', user ='root', password = '7777')
        if conn.is_connected():
            print("connected to mysql database")
    except Error as e:
        print(e)

    finally:
        conn.close()




class DbActions:


    def inp(self):
        pass
