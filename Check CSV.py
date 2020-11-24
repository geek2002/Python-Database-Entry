import csv
import os
def convertDate(date):
    date=date.split("/")
    Day = date[1].zfill(2)
    Month = date[0].zfill(2)
    Year = date [2].zfill(2)
    date = Day + "/" + Month + "/" + Year
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
        num=row[0][0:2]
        print(num + " %")
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
def changePhoneNumbers():
    f=open("Names.csv", encoding='utf-8-sig')
    n=open("Names New.csv","a", encoding='utf-8-sig')
    lines = f.readlines()

    for line in lines:
        row=line.split(",")
        number=row[5]
        number=number[1:(len(number)-1)]
        number=number.replace(" ", "")
        number=[number[0:5],number[4:10]]
        number=number[0] + " " + number[1]
        row[5]=number

        num=int(row[0])/1000
        print("Phone Number Check: "+ str(num)[0:4] + " %")


        line=",".join(row)
        n.write(line)
    n.close()

def formatCapitals():
    f=open("Names.csv", encoding='utf-8-sig')
    n=open("Names New.csv","a", encoding='utf-8-sig')
    lines = f.readlines()

    for line in lines:
        row=line.split(",")
        city=row[8]
        city=city.replace('"','')
        words=city.split()
        wordsTmp=[]
        for word in words:
            word=word.capitalize()
            wordsTmp.append(word)
        words=" ".join(wordsTmp)
        city=words
        num=int(row[0])/1000
        print("City Check: "+ str(num)[0:4] + " %")
        
        row[8]=city
        line=",".join(row)
        n.write(line + "\n")
    n.close()
def removeNewLine():
    f=open("Names.csv", encoding='utf-8-sig')
    n=open("Names New.csv","a", encoding='utf-8-sig')
    lines = f.readlines()

    for line in lines:
        row=line.split(",")
        rowlen=len(row)
        row[rowlen-1] = row[rowlen-1].replace("\n","")
        print(row[rowlen-1])
        line=",".join(row)
        n.write(line)
    n.close()
# checkLineLengths()
# changePhoneNumbers()
# formatCapitals()
removeNewLine()