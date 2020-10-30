
def getTables():
    testPyodbc()
    cursor = conn.cursor()
    tables = []
    for row in cursor.tables():
        tableName=row.table_name
        if "MS" not in tableName:
            tables.append(tableName)
            print(row.table_name)
    return tables
    pyodbc.Cursor.close()

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
        if File:
            print("Unknown Error Occured")
            driver=False
            
        else:
            print("File Not Found")
            driver=False
    return libary,driver
 
results=testPyodbc()
print("Libary: " + str(results[0]))
print("Driver: " + str(results[1]))