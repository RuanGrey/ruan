import mysql.connector

# Creates a connection
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Imastayer123"
)

# cursor is a kind of robot that does commands for you in the database
my_cursor = mydb.cursor()

# creates database
# my_cursor.execute("CREATE DATABASE users")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)