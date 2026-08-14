from pathlib import Path
import os

def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print (f"{i+1} : {items}")

def createfile():
    try: 
        readfileandfolder()
        name=input("Please tell your file name:")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write in this file?")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")

        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name=input("Please tell which file you want to read?")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)

            print("READED SUCCESSFULLY")

        else:
            print("FILE DOES NOT EXIST")

    except Exception as err:
        print(f"An error ocurred as {err}")

def updatefile():
    try: 
   
        readfileandfolder()
        name=input("Which file you want to update?")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of ur file.")
            print("Press 2 for overwriting the content of ur file.")
            print("Press 3 for appending  the data of ur file.")

            response=int(input("Enter your response:"))

            if response==1:
                name2=input("Tell your file new name?")
                p2=Path(name2)
                p.rename(p2)

            if response==2:
                with open(p,'w') as fs:
                    data=input("Tell what you want to overwrite?")
                    fs.write(data)

            if response==3:
                with open(p,'a') as fs:
                    data=input("Tell what you want to append in this file?")
                    fs.write(data)

    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name=input("Tell which file you want to delete?")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(name)

            print("FILE REMOVES SUCCESSFULLY")

        else:
            print("NO SUCH FILE EXISTS")

    except Exception as err:
        print(f"An error occured as {err}")
            
            
print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check=int(input("Please tell your response:"))

if check==1:
    createfile()

if check==2:
    readfile()

if check==3:
    updatefile()

if check==4:
    deletefile()


