import mysql.connector as mysql
from sql import *

#Before running or modifying. first run sql.py as to make database and then run this file.
#if database and table is created then run this.
db = mysql.connect(host = "localhost",user = "root", password = "", database = "collage")
command_handler = db.cursor(buffered=True)

def admin_session():
    print("Login success, Welcome admin!")
    while True:
        print("")
        print("Admin menu")
        print("1. Register new student")
        print("2. Register new teacher")
        print("3. Delete existing student")
        print("4. Delete existing teacher")
        print("5. Log out")
        user_opt = input(str("Option :"))
        if user_opt == "1":
            print("")
            print("Register new student")
            username = input(str("Student username :"))
            password = input(str("Student password :"))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES(%s,%s,'student')", query_vals)
            db.commit()
            print(username + " has been register as a student.")
        elif user_opt == "2":
            print("")
            print("Register new Teacher")
            username = input(str("Teacher username :"))
            password = input(str("Teacher password :"))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES(%s,%s,'teacher')", query_vals)
            db.commit()
            print(username + " has been register as a teacher3.")

        elif user_opt == "3":
            print("")
            print("Delete existing Student Account")
            username = input(str("Username :"))
            query_vals = (username, "student")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount<1:
                print("user not found")
            else :
                print("user " + username + " has been deleted.")
        elif user_opt == "4":
            print("")
            print("Delete existing Teacher Account")
            username = input(str("Username :"))
            query_vals = (username, "teacher")
            command_handler.execute("DELETE FROM users WHERE username = %s AND privilege = %s", query_vals)
            db.commit()
            if command_handler.rowcount < 1:
                print("user not found")
            else:
                print(username + " has been deleted.")
        elif user_opt == "5":
            print("Logging out")
            print("")
            break
        else :
            print("Invalid option, choose any one.")

def teacher_session():
    print("Login success, Welcome Teacher!")
    while True:
        print("")
        print("Teacher's menu")
        print("1. Mark student register")
        print("2. view register")
        print("3. Logout")

        user_opt = input(str("Option :"))
        if user_opt == "1":
            print("")
            print("Mark student register")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student'")
            records = command_handler.fetchall()
            date = input(str("Date : DD/MM/YY :"))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace("'","")
                record = str(record).replace("(","")
                record = str(record).replace(")","")
                #Present | Absent | Late
                status = input(str("status for "+ str(record) + "P/A/L :"))
                query_vals = (str(record),date,status)
                command_handler.execute("INSERT INTO attendence(username,date,status) VALUES(%s,%s,%s)", query_vals)
                db.commit()
                print(record+" Marked as " + status)
        elif user_opt == "2":
            print("")
            print("Viewing all student registers")
            command_handler.execute("SELECT username,date,status FROM attendence")
            records = command_handler.fetchall()
            print("Displaying all registers")
            for record in records:
                print(record)
        elif user_opt == "3":
            print("Logging out")
            break
        else :
            print("Invalid option")

def student_session(username):
    while True:
        print("")
        print("Student's Menu")
        print("1. View Register")
        print("2. Download Register")
        print("3. Log out")
        user_option = input(str("Option :"))
        if user_option == "1":
            print(username)
            print("Displaying registers")
            username = (str(username),)
            command_handler.execute("SELECT date, username, status FROM attendence WHERE username = %s",username)
            records = command_handler.fetchall()
            for record in records:
                print(record)

def auth_admin():
    print("")
    username = input(str("username :"))
    password = input(str("Password :"))
    if username == "admin":
        if password == "password":
            admin_session()
        else :
            print("Invalid password")
    else :
        print("Login detail not recogonised")

def auth_teacher():
    print("")
    username = input(str("username :"))
    password = input(str("password :"))
    query_vals = (username,password)
    command_handler.execute("SELECT * FROM users WHERE username = %s AND password = %s AND privilege = 'teacher'", query_vals)
    if command_handler.rowcount <= 0:
        print("login not recognised")
    else :
        print("Welcome Teacher")
        teacher_session()
def auth_student():
    print("")
    username = input(str("username :"))
    password = input(str("password :"))
    query_vals = (username,password,"student")
    command_handler.execute("SELECT username FROM users WHERE username=%s AND password=%s AND privilege=%s", query_vals)
    if command_handler.rowcount <= 0:
        print("Invalid Login details")
    else :
        student_session(username)

def main():
    while True:
        print("Welcome to our college")
        print("")
        print("1. Login as student ")
        print("2. Login as teacher ")
        print("3. Login as Admin ")

        user_option = input(">>>")
        if user_option == "1":
            print("Student login")
            auth_student()
        elif user_option == "2":
            print("Teacher login")
            auth_teacher()
        elif user_option == "3":
            print("Admin login")
            auth_admin()
        else :
            print("Invalid option")

main()
