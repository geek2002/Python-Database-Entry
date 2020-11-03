import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
odbc=[]
for x in installed_packages_list:
    if "odbc" in x:
        odbc.append(x.split("=")[0])

file=open("databaseLocation.txt","r")
databaseFile=file.readlines()[0]
file.close()
import pyodbc
try:
    pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseFile+';')
    driver = True
except pyodbc.InterfaceError:
    print("Driver Error")
    print("Unable to create tables automatically")
    print("Please create tables manually")
    driver=False