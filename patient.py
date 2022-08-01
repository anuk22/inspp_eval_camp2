import pyodbc
import sys
conString='Driver={SQL Server};Server=DESKTOP-MIIL0EB\SQLEXPRESS;Database=camp;Trusted_Connection=yes;'
myconn=pyodbc.connect(conString)
mycursor=myconn.cursor()
try:
    '''
    mycursor.execute("INSERT INTO patient VALUES(?,?,?,?)",('Abi','F',22,'A+'))
    mycursor.execute("INSERT INTO patient VALUES(?,?,?,?)",('Sej','M',65,'O+'))
    mycursor.execute("INSERT INTO patient VALUES(?,?,?,?)",('Shn','F',54,'AB-'))
    mycursor.execute("INSERT INTO patient VALUES(?,?,?,?)",('Ann','M',34,'B-'))
    mycursor.execute("INSERT INTO patient VALUES(?,?,?,?)",('Eli','M',28,'B+'))
    
    '''
except Exception as e:
    print(f"{type(e).__name__}")
    print(e)

def list():
    try:
        mycursor.execute("SELECT * FROM patient")
    except:
        print("failed to fetch data")
    else:
        print("ID   ","NAME  ","GENDER   ","AGE ","BLOOD_GROUP")
        for i in mycursor.fetchall():
            print(*i,sep="      ")
def add():
    try:
        patient_name=input("Enter Name of the Patient :")
        bloodgrp=input("Enter Blood Group :")
        gender=input("Enter Gender (M/F/T) :")
        age=int(input("Enter age :"))
        mycursor.execute("INSERT INTO patient VALUES(?,?,?,?)",(patient_name,gender,age,bloodgrp))
        myconn.commit()
    except :
        print(f"{type(e).__name__}")
        


def update():
    nm=int(input("Enter the id you want to update :"))
    try:
        mycursor.execute("SELECT * FROM patient WHERE id=(?)",(nm))
        name=input("Enter the updated name :")
        gen=input("Enter the updated gender :")
        ag=int(input("Enter the updated age :"))
        grp=input("Enter updated grp :")
        mycursor.execute("UPDATE patient SET patient_name=(?),gender=(?),age=(?),bloodgrp=(?) WHERE id=(?)",(name,gen,ag,grp,nm))
        myconn.commit()
    except Exception as e:
        print(f"{type(e).__name__}")

def delete():
    nm=input("Enter the id you want to delete")
    try:
        mycursor.execute("DELETE FROM patient WHERE id=(?)",(nm))
        myconn.commit()
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        if(mycursor.rowcount>0):
            print("Deleted")
        else:
            print(f"{nm} doesnt exists")
    
def SearchByID():
    nm=int(input("Enter the id you want to get details :"))
    try:
        mycursor.execute("SELECT * FROM patient WHERE id=(?)",(nm))
    except Exception as e:
        print(f"{type(e).__name__}")
    else:
        details=mycursor.fetchall()
        if(len(details)>0):
            print("ID   ","NAME  ","GENDER   ","AGE ","BLOOD_GROUP")
            for i in details:
                print(*i,sep="      ")
        else:
            print(f"{nm} is not found")
myconn.commit()

while True:
    ch=int(input("""Enter Your Choice
                     1.List All patients
                     2.Add 
                     3.Delete 
                     4.Search 
                     5.update
                     6.Exit\n"""))
    match ch:
        case 1:list()
        case 2:add()
        case 3:delete()
        case 4:SearchByID()
        case 5:update()
        case 6:sys.exit()
        case _:print("Invalid Input")

myconn.close()

