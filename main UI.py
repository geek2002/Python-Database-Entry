# --------- Imports ---------
import pypyodbc
import random
import os
import json

# --------- Global Varables ---------
cardsUsed=[]
namesUsed=[]
keys=[]
tables_dict={}
# --------- Link Access Driver  ---------
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Libarys\Documents\Microsoft Access\Test Database.accdb;')
cursor = conn.cursor()

# --------- Functions ---------
def loadJSON():
    with open('tables.json', 'r') as f:
        tables_dict = json.load(f)
        for x in tables_dict:
            print(x)
            keys.append(x)
        print(tables_dict)
    return tables_dict
def log(data):
    print(data)
def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
def convertDate(date):
    date=date.split("/")
    Day = date[1].zfill(2)
    Month = date[0].zfill(2)
    Year = date [2].zfill(2)
    date = Day + "/" + Month + "/" + Year
    return date
def addNames(ammount):
    keysIndex=0
    z=0
    for z in range(ammount):
        f=open("Names.csv", encoding='utf-8-sig')
        lines = f.readlines()
        x=0
        while x == 0:
            line=lines[random.randint(1,100000)]
            if line[0] in namesUsed:
                x=0
            else:
                x=1
        items=line.split(",")
        
        items[4] = items[4].upper()[0]
        items[5] = convertDate(items[5])
        items[8] = items[8][0:len(items[8])-1]
        x=0
        for x in range(len(items)):
            items[x]= "'" + items[x] + "'"
        namesUsed.append(items[0])
        items.remove(items[0])
        log(str(z) + "- Adding: " + items[2] + items[3])
        writeToDatabase(keysIndex,items)
        if z % 100 == True:
            writeToDatabase(keysIndex,items,True)
    writeToDatabase(keysIndex,items,True)
def writeToDatabase(tableIndex,data,commit=False):
    table=keys[tableIndex]
    feildNames=tables_dict[table]
    feildLen=len(feildNames)
    dataLen=len(data)
    if feildLen != dataLen:
        log("Feild and data lists are not the same length. Exiting")
    seperator = ","
    feilds=seperator.join(feildNames)
    values=seperator.join(data)
    sql="INSERT INTO " + table + "(" + feilds + ") VALUES(" + values + ")" 
    cursor = conn.cursor()
    cursor.execute(sql)
    if commit:
        conn.commit()
def Menu():
    print("")
    print("╔═══════════════════════════════════════╗")
    print("║          1:Enter Names                ║")
    print("║          2:Enter Cards                ║")
    print("║          3:Enter Sales                ║")
    print("║          4:Exit                       ║")
    print("╚═══════════════════════════════════════╝")
    do=input("> ")
    if do == "1":
        clean()
        addNames(int(input("How Many? >> ")))
    elif do == "2":
        clean()
        Menu()
    elif do == "3":
        clean()
        Menu()
    elif do == "4":
        exit()
    else:
        print("Error , Please only use 1,2,3 or 4")
        Menu()
tables_dict=loadJSON()
Menu()
