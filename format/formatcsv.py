import csv

cities = []
def formatDate(date):
    dateIn=date.split("/")
    dateTemp=[dateIn[2],dateIn[0],dateIn[1]]
    dateOut="/".join(dateTemp)
    return dateOut
def breakOutCity():
    f=open("format/OldNames.csv", encoding='utf-8-sig')
    lines = f.readlines()
    for line in lines:
        items=line.split(",")
        city=items[5].split("\n")[0]
        formatString(city)
def formatString(string):
    if len(string) < 11:
        string=string.lower()
        stringTemp=[]
        for x in string:
            if x != '"':
                stringTemp.append(x)
        stringTemp[0] = stringTemp[0].upper()

        if " " in stringTemp:
            spaceIndex=stringTemp.index(" ")
            stringTemp[spaceIndex+1]=stringTemp[spaceIndex+1].upper()
        stringTemp="".join(stringTemp)
        print(stringTemp)
        writeCity(stringTemp)
def writeCity(city):
    newfile=open("Cities.txt","a")
    newfile.write(city)
    newfile.write("\n")
    newfile.close()
def formatFile():
    f=open("format/OldNames.csv", encoding='utf-8-sig')
    lines = f.readlines()
    for line in lines:
        items=line.split(",")
        newLine=",".join(items[0:5])
        print(newLine)
    nf=open("format/NewNames.csv", encoding='utf-8-sig',"a")
    nf.write(newLine)
    nf.write("\n")
formatFile()