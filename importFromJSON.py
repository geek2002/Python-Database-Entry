import json
keys=[]
with open('tables.json', 'r') as f:
    tables_dict = json.load(f)
for x in tables_dict:
    print(x)
    keys.append(x)

index=int(input("Enter Index >> "))
mykey=keys[index]
for x in tables_dict[mykey]:
    print(x)