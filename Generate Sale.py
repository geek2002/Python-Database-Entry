import pyodbc
import random
file=open("databaseLocation.txt","r")
databaseFile=file.readlines()[0]
file.close()
conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ='+databaseFile+';')
cursor = conn.cursor()
def getCustomers():
    cursor.execute('select cust_id from customer')
    customers=len(cursor.fetchall())
    return customers
def getStaff():
    cursor.execute("select staff_id from staff WHERE staff_role='Checkouts'")
    staff=len(cursor.fetchall())
    return staff
def getProducts():
    cursor.execute('select * from product')
    products=cursor.fetchall()
    return products
def getCards(customer):
    cursor.execute("select card_id from card WHERE cust_id=" + str(customer))
    fetch=cursor.fetchall()
    cards=[]
    for card in fetch:
        card=str(card).split(",")
        card=int(card[0][1:])
        cards.append(card)
    return cards
def generateSale():
    numberOfItems=random.randint(1,(len(products)*5))
    staffMember=random.randint(1,staff)
    customer=random.randint(1,customers)
    card=random.choice(getCards(customer))
    print(card)

customers=getCustomers()
products=getProducts()
staff=getStaff()
generateSale()
