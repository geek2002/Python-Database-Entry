import pypyodbc
import json

with open('tables copy.json', 'r') as f:
        tables_dict = json.load(f)

conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Libraries\Documents\Microsoft Access\Test Database.accdb;')
cursor = conn.cursor()

",".join(tables_dict["customer"][""])
cursor.execute("CREATE TABLE Persons (Personid AUTOINCREMENT PRIMARY KEY,LastName varchar(255) NOT NULL,FirstName varchar(255),Age int);")
conn.commit()

