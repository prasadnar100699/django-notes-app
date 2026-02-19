import os
import MySQLdb

db_host = os.environ.get("DB_HOST")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_name = os.environ.get("DB_NAME")

connection = MySQLdb.connect(
    host=db_host,
    user=db_user,
    passwd=db_password,
)

cursor = connection.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name};")
connection.commit()
cursor.close()
connection.close()

print(f"Database '{db_name}' ensured.")
