import mysql.connector
import config

connection = mysql.connector.connect(**config.connection())

def get_data(query):
    '''This function returns the data from the database'''
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    return data

def select_all(number):
    '''This function returns all the data from the database'''
    query = 'SELECT * FROM employees LIMIT %s' % number
    return get_data(query)

if __name__=='__main__':
    print(select_all(20))
   
