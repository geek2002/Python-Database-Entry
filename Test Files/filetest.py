def log(data):
    print(data)
    file=open("Log","a")
    file.write(data)
    file.write("\n")
    file.close()

log("Functionality: ")
log("╔═══════════════════════════════════════╗")
log("║          1:Enter Names                ║")
log("║          2:Enter Cards                ║")
log("║          3:Enter Sales                ║")
log("║          4:Get Tables                 ║")
log("║          5:Exit                       ║")
log("╚═══════════════════════════════════════╝")