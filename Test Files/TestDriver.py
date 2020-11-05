import os
import sys
functionality=0
def installModule(moduleName):
    os.system("pip install " + moduleName )
def getDatabaseLocation():
    if os.path.exists("databaseLocation.txt"):
        file=open("databaseLocation.txt","r")
        databaseFile=file.readlines()[0]
        file.close()
    return databaseFile
def testPyodbc(databaseLocation):
    try:
        import pyodbc
        print("Libary: OK")
    except ModuleNotFoundError:
        print("Unable to import Module")
        print("Reason: Module Not found")
        input("Press <Enter> to install")
        installModule("pyodbc")
        testPyodbc(databaseLocation)
    try:
        pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseLocation+';')
        print("Driver: OK")
        functionality= 2
    except pyodbc.InterfaceError:
        print("Driver Error")
        print("Unable to user pyodbc resorting to backup libary (pypyodbc) limited functionality")
        testPypyodbc(databaseLocation)
    except pyodbc.Error:
        if os.path.exists(databaseLocation):
            print("An Unknown Error occured, Please Try Again")
        else:
            print("File Not Found, change file location and try again")
    return functionality
def testPypyodbc(databaseLocation):
    try:
        import pypyodbc
        print("Libary: OK")
        functionality = 1
    except ModuleNotFoundError:
        print("Unable to import Module")
        print("Reason: Module Not found")
        input("Press <Enter> to install")
        installModule("pypyodbc")
        testPypyodbc(databaseLocation)
    return functionality

databaseLocation = getDatabaseLocation()
testPyodbc(databaseLocation)
