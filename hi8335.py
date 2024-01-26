import subprocess

matrix = ["cmatrix", "-a"]

subprocess.run("clear")
def menu():
    print("██╗  ██╗██╗ █████╗ ██████╗ ██████╗ ███████╗")
    print("██║  ██║██║██╔══██╗╚════██╗╚════██╗██╔════╝")
    print("███████║██║╚█████╔╝ █████╔╝ █████╔╝███████╗")
    print("██╔══██║██║██╔══██╗ ╚═══██╗ ╚═══██╗╚════██║")
    print("██║  ██║██║╚█████╔╝██████╔╝██████╔╝███████║")
    print("╚═╝  ╚═╝╚═╝ ╚════╝ ╚═════╝ ╚═════╝ ╚══════╝")
    print("")
    print("Pick a number")
    print("")
    print("1. cmatrix")
    print("2. btop")
    print("3. Discord")
    print("4. Steam")
    print("5. Exit")
    menu1 = input("user@hi8335:~$ ")
    if menu1 == "1":
        subprocess.run("clear")
        subprocess.run(matrix)
    elif menu1 == "2":
        subprocess.run("clear")
        subprocess.run("btop")
    elif menu1 == "3":
        subprocess.run("clear")
        subprocess.run("discord")
    elif menu1 == "4":
        subprocess.run("clear")
        subprocess.run("steam")
    elif menu1 == "5":
        subprocess.run("clear")
        print("See you later ;)")
       
    else:
        subprocess.run("clear")
        print("Wrong, choose again")
        print("")
        menu()

menu()