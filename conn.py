# import mysql.connector
# import mysql.connector.errorcode


# def connect():
#     try:
#         conn = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             passwd="",
#             database="employees"
#         )
#     except mysql.connector.Error as err:
#         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#             print("Something is wrong with your user name or password")
#         elif err.errno == errorcode.ER_BAD_DB_ERROR:
#             print("Database does not exist")
#         else:
#             print(err)
#     else:
#         conn.close()

# connect()