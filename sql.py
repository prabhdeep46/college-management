import mysql.connector as mysql

try :
    db = mysql.connect(host="localhost",user="root",password="")
    command_handler = db.cursor()
    command_handler.execute("CREATE DATABASE college")
    print("Database is created. creating Tables")
except Exception as e:
    print(e)
    print("Database could not created")

try:
    db1 = mysql.connect(host="localhost", user="root", password="", database="college")
    command_handler = db1.cursor()
    command_handler.execute(
        "CREATE TABLE users(ID INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(35), password VARCHAR(255), privilege VARCHAR(20)")
    print("Table created created")
except Exception as e:
    print(e)
    print("Table could not be created")
