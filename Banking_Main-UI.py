# --------- Imports ---------
import random
import os
import json
def Menu():
    log("Functionality: " + func[functionality])
    log("╔═══════════════════════════════════════╗")
    log("║          1:Enter Names                ║")
    log("║          2:Enter Cards                ║")
    log("║          3:Enter Sales                ║")
    log("║          4:Add Tables                 ║")
    log("║          5:Exit                       ║")
    log("╚═══════════════════════════════════════╝")
    do=input("> ")
    if do == "1":
        clean()
        addNames(int(input("How Many? >> ")))
    elif do == "2":
        clean()
        generateCards(int(input("How Many? >> ")),22,2020)
    elif do == "3":
        clean() 
        Menu()
    elif do == "4":
        addTables()
    elif do == "5":
        exit()
    else:
        log("Error , Please only use 1,2,3 or 4")
        Menu()