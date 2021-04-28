# --------- Imports ---------
import random
import os
import json
import pyodbc


def log(data):
    print(data)
    # file=open("Log.txt","a")
    # file.write(str(data))
    # file.write("\n")
    # file.close()
def formatEmail(email):
    domains=["gmail.com","yahoo.com","hotmail.com","hotmail.co.uk","msn.com","yahoo.co.uk","live.com","outlook.com","googlemail.com","icloud.com"]
    emailPrefix=email.split("@")[0]
    email=emailPrefix + "@" + domains[int(random.randint(0,18)/2)]
    return email
def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
def formatDate(date):
    dateIn=date.split("/")
    dateTemp=[dateIn[2],dateIn[0],dateIn[1]]
    dateOut="/".join(dateTemp)
    return dateOut
def Menu():
    log("╔═══════════════════════════════════════╗")
    log("║          1:Generate Customers         ║")
    log("║          2:Generate Accounts          ║")
    log("║          3:Generate Transactions      ║")
    log("║          4:Generate Branches          ║")
    log("║          5:Exit                       ║")
    log("╚═══════════════════════════════════════╝")
    do=input("> ")
    if do == "1":
        clean()
        createCustomer(30)
    elif do == "2":
        clean()
        createAccount()
    elif do == "3":
        clean() 
        createTransaction()
    elif do == "4":
        createBranch(10)
    elif do == "5":
        exit()
    else:
        log("Error , Please only use 1,2,3 or 4")
        Menu()
def createCustomer(ammount):
    for a in range(ammount):
        fname=""
        lname=""
        dob=""
        email=""
        branID=str(random.randint(0,9))
        passcode=str(random.randint(11111111,99999999))
        custType="normal"
        avatar=str(random.randint(0,5))
        f=open("Names.csv", encoding='utf-8-sig')
        lines = f.readlines()
        items=lines[random.randint(1,2000)].split(",")
        fname=items[1]
        lname=items[2]
        dob=formatDate(str(items[3]))
        email=formatEmail(items[4])
        values=[fname,lname,dob,email,branID,passcode,custType,avatar]
        values="'" + "','".join(values) + "'"
        sql="INSERT INTO customer(cust_fname, cust_lname, cust_dob, cust_email, cust_bran_ID, cust_passcode, cust_type, cust_avatar) VALUES(" + values + ");" 
        print(sql)
        sqlfile=open("sqlfile.txt","a")
        sqlfile.write(sql)
        sqlfile.write("\n")
        sqlfile.close()
def generateBranchName(city):
    prefix=["North", "South", "East", "West"]
    suffix=["Town Centre","Branch", "District"]
    if random.randint(1,2) == 1:
        name = prefix[random.randint(0,len(prefix)-1)] + " " + city
    else:
        name = city + " " + suffix[random.randint(0,len(suffix)-1)]
    return name
def createBranch(number):
    usedCities=[] 
    for a in range(number):
        name=""
        location=""
        f=open("Cities.txt", encoding='utf-8-sig')
        lines = f.readlines()
        while True:
            city=lines[random.randint(1,1945)]
            if city not in usedCities:
                usedCities.append(city)
                break
        location = city
        name=generateBranchName(location)
        values=[name,location]
        values="'" + "','".join(values) + "'"
        sql="INSERT INTO customer(bran_name, bran_location) VALUES(" + values + ");" 
        print(sql)
        sqlfile=open("sqlfile.txt","a")
        sqlfile.write(sql)
        sqlfile.write("\n")
        sqlfile.close()
def createAccount(number):
    usedCities=[] 
    for a in range(number):

        #select a customer
        #decide how many accounts
        #
        displayName=""

        accoType=""

        balance=""

        status=""
        customer=""
        






        values=[name,location]
        values="'" + "','".join(values) + "'"
        sql="INSERT INTO customer(bran_name, bran_location) VALUES(" + values + ");" 
        print(sql)
        sqlfile=open("sqlfile.txt","a")
        sqlfile.write(sql)
        sqlfile.write("\n")
        sqlfile.close()
def createTransaction():
    print("Create Transaction")
Menu()