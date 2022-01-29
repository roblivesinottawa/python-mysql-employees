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

def assistant_engineer():
    '''returns all employees whose job title is assistant engineer'''
    query = '''SELECT * FROM employees e 
                WHERE EXISTS (
                    SELECT * FROM titles t
                    WHERE t.emp_no = e.emp_no AND title = 'assistant engineer');'''
    return get_data(query)

def select_employees():
    '''creates a procedure that returns 1000 employees'''
    query = ''' DELIMITER $$
                CREATE PROCEDURE select_employees()
                BEGIN
                    SELECT * FROM employees LIMIT 1000;
                END$$
                DELIMITER ;
                '''
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.callproc('select_employees')
    data = cursor.fetchall()
    return data

def average_salary():
    '''returns the average salary of employees'''
    query = '''
            DELIMITER $$
            CREATE PROCEDURE average_salary()
            BEGIN
                SELECT 
                    AVG(salary)
                FROM
                    salaries;
            END$$
            DELIMITER ;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.callproc('average_salary')
    data = cursor.fetchall()
    return data

                

if __name__=='__main__':
    # print(select_all(20))
    # print(assistant_engineer())
    # print(select_employees())
    print(average_salary())
   