import sys
import os
import json

DB_FILE = "data.json"


def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return []


def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)

myuserdb = load_db()

def login():
    os.system("cls")
    print('================login============')
    os.system("color 0A") 
    name = input("enter username: ")
    password = input("enter password: ")
    
    for i in myuserdb:
        if i["username"] == name and i["password"] == password:
            print("login successful")
            return
    os.system("cls")
    os.system("color 0C")
    print("login denied, first you need to create an account")

def signup():
    print("signup")  
    os.system("color 0A")
    while True:
        uname = input("type unique username: ")
        if any(i["username"] == uname for i in myuserdb):
            os.system("color 0C")
            print("username already exists")
            continue
        
        password = input("type password: ")
        phone = int(input("type phone number: "))
        gmail = input("type gmail: ")
        school = input("type your school name: ")
        
        temp = {
            "username": uname,
            "password": password,
            "phone": phone,
            "gmail": gmail,
            "school": school
        }
        myuserdb.append(temp)
        save_db(myuserdb)  
        os.system("color 0D")
        os.system("cls")
        print("database updated with new user")
        print(myuserdb)
        break

if len(sys.argv) > 1:
    if sys.argv[1] == "login":
        login()
    elif sys.argv[1] == "signup":
        signup()
