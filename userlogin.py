# login signup in cli

import sys
import os

os.system("cls")
username=None
password = None

myuserdb = [ {'username': 'mohit', 'password': '1234', 'phone': 6373453454, 'gmail': 'mohit@gmail.com', 'school': 'clc alwar'},
             {'username': 'ronak', 'password': 'ronak123', 'phone': 8998293842, 'gmail': 'sjpw@gmail.com', 'school': 'vps alwar'},
              {'username': 'Akhil', 'password': 'DEVIL', 'phone': 7737453456, 'gmail': 'donk@gmail.com', 'school': 'aps alwar'}]

def login():
     print("=======================================================")
     print("========================login=========================")  
     print("=======================================================")
     os.system("color 0A") 
     name = input("enter username :")

     password = input("enter password")
     login_status = 0 
     for i in myuserdb:
         if i["username"]== name and i['password']==password:
             login_status=True
     if login_status == True:
         print("login succesfull")
     else:
         os.system("cls")
         os.system('color 0C')
         print("login denied first you need to create an account")
     return 0;  




def signup():
    print("=======================================================")
    print("========================signup=========================")  
    print("=======================================================")
    os.system("color 0A")
    Flag = True
    while Flag:
        uname = input("type uniq user name: ")
        mach = 0
        for i in myuserdb:
            if i["username"] == uname:
                mach = 1
                os.system("color 0C")
                print("username already exists")
                break
        
        if mach == 0:  # only create new user if username not found
            os.system("color 0A")
            os.system("cls")
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
            os.system("color 0D")
            os.system("cls")
            print("database updated with new user")
            print(myuserdb)

            Flag = False  # exit loop after successful signup
    return 0


if sys.argv[1]=="login":
   login()
elif sys.argv[1]=="signup":
    signup()
