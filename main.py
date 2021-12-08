import mysql.connector

employees_db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysqlpassmacrob",
    database="employees"
)

cursor = employees_db.cursor()

def show_databases():
    """This function will show the databases as a list when invoked."""
    cursor.execute("SHOW DATABASES")
    [print(db) for db in cursor]


cursor.execute('USE employees;')

def show_tables():
    """This function will show all the tables in the selected database."""
    cursor.execute("SHOW TABLES")
    [print(table) for table in cursor]


def show_employees():
    """This function will display all employees in the database with an added constraint"""
    cursor.execute("SELECT * FROM employees LIMIT 20")
    [print(e) for e in cursor]

def show_employees_by_first_name(fname):
    """This function will display all employees with a given first name.""" 
    cursor.execute("SELECT * FROM employees WHERE first_name = %s", (fname,))
    [print(e) for e in cursor]

def emps_with_same_salary():
    """This function will display all employees with the same salary."""
    cursor.execute("""SELECT salary, 
                    COUNT(emp_no) AS employees_with_same_salary 
                    FROM salaries WHERE salary > 80000 
                    GROUP BY salary ORDER BY salary LIMIT 20;""")
    print("emp_no, employees_with_same_salary")
    [print(e) for e in cursor]

def avg_salary_higher_than_120000():
    """This function will display the average salary of employees with a salary higher than 120000."""
    cursor.execute("""SELECT emp_no, AVG(salary) AS avg_salary 
                    FROM salaries GROUP BY emp_no
                    HAVING AVG(salary) > 120000
                    ORDER BY emp_no LIMIT 20;""")
    print("emp_no, avg_salary")
    [print(e) for e in cursor]

def employees_signed_more_than_1():
    """This function selects all employees who have signed more than one contract after 01-01-2000"""
    cursor.execute('''
    SELECT emp_no FROM dept_emp 
    WHERE from_date > '2000-01-01' 
    GROUP BY emp_no 
    HAVING COUNT(from_date) > 1 ORDER BY emp_no''')
    [print(e) for e in cursor]

def insert_employee():
    cursor.execute(
    """
    INSERT INTO employees
    (emp_no, birth_date, first_name, last_name, gender, hire_date)
    VALUES
    (999904, '1977-09-14', 'John', 'Cree', 'M', '1999-10-01');
    """
    )
    employees_db.commit()
    print("Inserted employee with emp_no 999903")
    [print(e) for e in cursor]

if __name__ == "__main__":
    # show_databases()
    show_tables()
    # show_employees()
    # show_employees_by_first_name('Elvis')
    # emps_with_same_salary()
    # avg_salary_higher_than_120000()
    # employees_signed_more_than_1()
    # insert_employee()



