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

# --------- Check Files  ---------
def changeLocation():
    print("Database File Not Found")
    print("Please enter Database File Location")
    databaseFile=input(">> ")
    locaFile=open("databaseLocation.txt","w")
    locaFile.write(databaseFile)
    locaFile.close()
    return databaseFile

if os.path.exists("databaseLocation.txt"):
    file=open("databaseLocation.txt","r")
    databaseFile=file.readlines()[0]
    file.close()
    fileExists = os.path.exists(databaseFile)
    if fileExists == False:
        changeLocation()
else:
    databaseFile=changeLocation()


# --------- Link Access Driver  ---------
conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseFile+';')
cursor = conn.cursor()

# --------- Functions ---------
def Menu():
    print("")
    print("╔═══════════════════════════════════════╗")
    print("║          1:Enter Names                ║")
    print("║          2:Enter Cards                ║")
    print("║          3:Enter Sales                ║")
    print("║          4:Get Tables                 ║")
    print("║          5:Exit                       ║")
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
        getTables()
    elif do == "5":
        exit()
    else:
        print("Error , Please only use 1,2,3 or 4")
        Menu()
def log(data):
    print(data)
def clean():
    os.system('cls' if os.name == 'nt' else 'clear')
def loadJSON():
    with open('tables.json', 'r') as f:
        tables_dict = json.load(f)
        for x in tables_dict:
            keys.append(x)
    return tables_dict
def convertDate(date):
    date=date.split("/")
    Day = date[1].zfill(2)
    Month = date[0].zfill(2)
    Year = date [2].zfill(2)
    date = Day + "/" + Month + "/" + Year
    return date
def createTable():
    sql="CREATE TABLE"
    for x in tables_dict:
        sql=sql + " " + x + " (" + x + "_id AUTOINCREMENT PRIMARY KEY,"
        feilds=tables_dict[x]["feilds"]
        dataTypes=tables_dict[x]["dataTypes"]
        y=0
        for y in range(len(feilds)):
            if y != (len(feilds)-1):
                sql=sql + feilds[y] + " " + dataTypes[y] + " , "
            else:
                sql=sql + " " + feilds[y] + " " + dataTypes[y] + ") "
        cursor.execute(sql)
        print(sql)
        sql="CREATE TABLE"
        conn.commit()
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
    cursor.execute(sql)
    if commit:
        conn.commit()
def testPyodbc():
    try:
        import pyodbc
        libary = True
    except ModuleNotFoundError:
        print("pyodbc libary not installed please run 'pip install pyodbc' to install")
        libary = False
    
    try:
        pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseFile+';')
        driver = True
    except pyodbc.InterfaceError:
        print("Driver Error")
        print("Unable to create tables automatically")
        print("Please create tables manually")
        driver=False
    except pyodbc.Error:
        if os.path.exists(databaseFile):
            print("Unknown Error Occured")
            driver=False
            
        else:
            print("File Not Found")
            driver=False
    return libary,driver
def getTables():
    curs = conn.cursor()
    tables = []
    for row in curs.tables():
        tableName=row.table_name
        if "MS" not in tableName:
            tables.append(tableName)
            print(row.table_name)
    cursor.close()
    return tables
    

tables_dict=loadJSON()
Menu()
