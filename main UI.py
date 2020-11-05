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
functionality = 0
func=["None","Limited","Full"]
# --------- Functions ---------
def Menu():
    log("Functionality: " + func[functionality])
    log("╔═══════════════════════════════════════╗")
    log("║          1:Enter Names                ║")
    log("║          2:Enter Cards                ║")
    log("║          3:Enter Sales                ║")
    log("║          4:Get Tables                 ║")
    log("║          5:Exit                       ║")
    log("╚═══════════════════════════════════════╝")
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
        log("Error , Please only use 1,2,3 or 4")
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
        log(sql)
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
def changeLocation():
    log("Database File Not Found")
    log("Please enter Database File Location")
    databaseFile=input(">> ")
    locaFile=open("databaseLocation.txt","w")
    locaFile.write(databaseFile)
    locaFile.close()
    return databaseFile
def getDatabaseLocation():
    if os.path.exists("databaseLocation.txt"):
        file=open("databaseLocation.txt","r")
        databaseFile=file.readlines()[0]
        file.close()
        fileExists = os.path.exists(databaseFile)
        if fileExists == False:
            changeLocation()
    else:
        databaseFile=changeLocation()
    return databaseFile 
def getTables():
    curs = conn.cursor()
    tables = []
    for row in curs.tables():
        tableName=row.table_name
        if "MS" not in tableName:
            tables.append(tableName)
            log(row.table_name)
    cursor.close()
    return tables

def installModule(moduleName):
    os.system("pip install " + moduleName)
def testPyodbc(databaseLocation):
    try:
        import pyodbc
        log("Libary: OK")
    except ModuleNotFoundError:
        log("Unable to import Module")
        log("Reason: Module Not found")
        input("Press <Enter> to install")
        installModule("pyodbc")
        testPyodbc(databaseLocation)
    try:
        pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseLocation+';')
        log("Driver: OK")
        functionality= 2
    except pyodbc.InterfaceError:
        log("Driver Error")
        log("Unable to user pyodbc resorting to backup libary (pypyodbc) limited functionality")
        functionality = testPypyodbc(databaseLocation)
    except pyodbc.Error:
        if os.path.exists(databaseLocation):
            log("An Unknown Error occured, Please Try Again")
        else:
            log("File Not Found, change file location and try again")
    return functionality
def testPypyodbc(databaseLocation):
    try:
        import pypyodbc
        log("Libary: OK")
        functionality= 1
    except ModuleNotFoundError:
        log("Unable to import Module")
        log("Reason: Module Not found")
        input("Press <Enter> to install")
        installModule("pypyodbc")
        testPypyodbc(databaseLocation)
    return functionality

databaseFile=getDatabaseLocation()
functionality = testPyodbc(databaseFile)

# --------- Link Access Driver  ---------
if functionality == 2:
    import pyodbc
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseFile+';')
elif functionality == 1:
    import pypyodbc
    conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseFile+';')
else:
    log("An error has accured please try again, if this error continues please report on github")
cursor = conn.cursor()

tables_dict=loadJSON()
Menu()
