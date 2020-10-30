import pypyodbc
import json

with open('tables copy.json', 'r') as f:
        tables_dict = json.load(f)


conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Libarys\Documents\Microsoft Access\Test Database.accdb;')
cursor = conn.cursor()
#cursor.execute("CREATE TABLE Persons (Personid AUTOINCREMENT PRIMARY KEY,LastName varchar(255) NOT NULL,FirstName varchar(255),Age int);")

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

createTable()