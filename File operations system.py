from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))

    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def createfile():
    try:
        readfileandfolder()

        name = input("Please tell your file name: ")
        p = Path(name)

        if not p.exists():
            with open(p, "w") as fs:
                data = input("What you want to write in this file? ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")

        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()

        name = input("Please tell which file you want to read? ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p, 'r') as fs:
                data = fs.read()
                print(data)

            print("READ SUCCESSFULLY")

        else:
            print("FILE DOES NOT EXIST")

    except Exception as err:
        print(f"An error occured as {err}")


def updatefile():
    try:
        readfileandfolder()

        name = input("Which file you want to update? ")
        p = Path(name)

        if p.exists() and p.is_file():

            print("Press 1 for changing the name of your file.")
            print("Press 2 for overwriting the content of your file.")
            print("Press 3 for appending the data of your file.")

            response = int(input("Enter your response: "))

            if response == 1:
                name2 = input("Tell your file new name? ")
                p2 = Path(name2)
                p.rename(p2)
                print("FILE NAME CHANGED SUCCESSFULLY")

            elif response == 2:
                with open(p, 'w') as fs:
                    data = input("Tell what you want to overwrite? ")
                    fs.write(data)

                print("FILE UPDATED SUCCESSFULLY")

            elif response == 3:
                with open(p, 'a') as fs:
                    data = input("Tell what you want to append in this file? ")
                    fs.write(data)

                print("DATA APPENDED SUCCESSFULLY")

            else:
                print("INVALID CHOICE")

        else:
            print("FILE DOES NOT EXIST")

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        readfileandfolder()

        name = input("Tell which file you want to delete? ")
        p = Path(name)

        if p.exists() and p.is_file():
            os.remove(name)

            print("FILE REMOVED SUCCESSFULLY")

        else:
            print("NO SUCH FILE EXISTS")

    except Exception as err:
        print(f"An error occured as {err}")


# Main Menu

while True:

    print("\n--------------------------------")
    print("       FILE MANAGEMENT SYSTEM")
    print("--------------------------------")

    print("Press 1 for creating a file")
    print("Press 2 for reading a file")
    print("Press 3 for updating a file")
    print("Press 4 for deleting a file")
    print("Press 5 for exit")

    check = int(input("Please tell your response: "))

    if check == 1:
        createfile()

    elif check == 2:
        readfile()

    elif check == 3:
        updatefile()

    elif check == 4:
        deletefile()

    elif check == 5:
        print("PROGRAM CLOSED")
        break

    else:
        print("INVALID CHOICE")


