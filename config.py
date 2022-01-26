def connection():
    """
    This function returns the connection to the database.
    """
    config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysqlpassmacrob',
    'database': 'employees',
    'raise_on_warnings': True
}
    return config



