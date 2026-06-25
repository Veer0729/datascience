# Expection Handling

# a = int(input("Enter a number: "))

# try:
#     print(10/a)

# except Exception as err:
#     print(f"sorry you have a error named {err}")

# else:
#     print("good there is no error")

# print("divison done!")


# file handling

# p = open(r"C:\Users\dell\Documents\git --version.txt")
# print(p.read())

# r = open("superman.txt","w")
# r = open("superman.txt","a")
# r.write("let's add some new content")
# r.close()

from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1}: {items} ")


def createfile():
    try:
        readfileandfolder()
        name = input("enter the name of your file: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("what you want to write in this file: ")
                fs.write(data)
        else:
            print("this file already exists")

        print(f"file created succesfully!!")

    except Exception as err:
        print(f"an error occoured named: {err}")

def readfile():
    readfileandfolder()
    name = input("which file you want to read?: ")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p, "r") as fs:
            data = fs.read()
            print(data)
    else:
        print("couldn't find file....recheak the name plz")

def updatefile():
    readfileandfolder()
    name = input("name of the file you want to update: ")
    p = Path(name)
    if p.exist() and p.is_file:
        changes = int(input("Press 1 if you want to change the file's name""/n" "Press 2 if you want to update the text content" "/n" "Press 3 if you want to overwrite everything: "))

    if changes == 1:
        name2 = input("enter new name: ")
        p2 = Path(p2)
        p.rename(p2)

    if changes == 2:
        with open(p, "a") as fs:
            data = input("what do you wanna write?: ")
            fs.write(" "+ data)

    if changes == 3:
        with open(p, "w") as fs:
            data = input("what do you wanna write?: ")
            fs.write(data)

def deletefile():
    readfileandfolder()
    name = input("which file you wanna remove?: ")
    p = Path(name)

    if p.exists() and p.is_file():
        os.remove(p)
        print("file deleted")
    else:
        print("file doesnt exists")



print("1 for creating a file")
print("2 for reading a file")
print("3 for updating a file")
print("4 for deleation a file")
print("5 to quit")
check = int(input("Enter a number plz: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()

if check == 5:
    quit()