import csv
import os
def convertDate(date):
    date=date.split("/")
    Day = date[1].zfill(2)
    Month = date[0].zfill(2)
    Year = date [2].zfill(2)
    date = Day + "/" + Month + "/" + Year
    print(date)
    return date
def formatCSV():
    f=open("Names.csv", encoding='utf-8-sig')
    n=open("Names New.csv","a", encoding='utf-8-sig')
    lines = f.readlines()

    for line in lines:
        row=line.split(",")
        row[5]=convertDate(row[5])
        line=",".join(row)
        n.write(line)
    n.close()
def checkLineLengths():
    file=open("Names.csv", encoding='utf-8-sig')
    lines = file.readlines()
    errors=[]
    for line in lines:
        row=line.split(",")
        num=row[0][0:2]
        print(num + " %")
        if len(row) != 9:
            errors.append(row[0])
    print(errors)
checkLineLengths()