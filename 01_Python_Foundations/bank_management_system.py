import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data =  json.loads(fs.read())
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits, k =3)
        spchar = random.choices("!@#$%&*", k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createacc(self):
        info = {
            "name": input("Tell your name :- "),
            "age" : int(input("tell your age :- ")),
            "email": input("tell your email :- "),
            "pin": int(input("tell your 4 number pin :- ")),
            "accountNo." : Bank.__accountgenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Can't create ur acc")
        else:
            print("acc created")
            for i in info:
                print(f"{i}:{info[i]}")
            print("plz note down ur acc number")
            Bank.data.append(info)  
            Bank.__update()

    def deposit(self):
        accnum = input("enter acc number")
        pin = input("enter pin number")

        userdata = [i for i in Bank.data if i['accountNO.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")

        else:
            amount = int(input("how much amount to deposit"))
            if amount < 0:
                print("nope..can't do negative numbers")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()

    def withdraw(self):
        accnum = input("enter acc number")
        pin = input("enter pin number")

        userdata = [i for i in Bank.data if i['accountNO.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")

        else:
            amount = int(input("how much amount to deposit"))
            if amount > userdata[0]['balance']:
                print("nope...u are poor for that")

            else:
                userdata[0]['balance'] -= amount
                Bank.__update()

    def details(self):
        accnum = input("enter acc number")
        pin = input("enter pin number")

        userdata = [i for i in Bank.data if i['accountNO.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")

        else:
            print("u r info are: ")
            for i in userdata[0]:
                print(f"{i} : {userdata}[0][i]")

    def update1(self):
        accnum = input("enter acc number")
        pin = input("enter pin number")

        userdata = [i for i in Bank.data if i['accountNO.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")

        else:
            print("you can only update ur name, gmail and password")

            newdata = {
                "name": input("enter new name: "),
                "email": input("enter new email: "),
                "pin": input("enter new pin: ")
            }

            if newdata["name"] == "":
                newdata["name"] == userdata[0]["name"]
            if newdata["email"] == "":
                newdata["email"] == userdata[0]["email"]
            if newdata["pin"] == "":
                newdata["pin"] == userdata[0]["pin"]
            
            newdata["age"] = userdata[0]["age"]
            newdata["balance"] = userdata[0]["balance"]
            newdata["accountNo."] = userdata[0]["accountNo."]

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()

    def delete():

        accnum = input("enter acc number")
        pin = input("enter pin number")

        userdata = [i for i in Bank.data if i['accountNO.'] == accnum and i['pin'] == pin]

        if userdata == False:
            print("sorry no data found")

        else:
            check = input("u sure u wanna delete ur acc?? [press y to confirm]: ")
            if check == 'y' or check == "Y":
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("acc deleted")
                Bank.__update()
            else:
                print("bypassed")

user = Bank()
print("press 1 for acc creation")
print("press 2 for acc deposit")
print("press 3 for acc withdrawl")
print("press 4 for acc details")
print("press 5 for acc update")
print("press 6 for acc deleation")

check = int(input("Enter your response: "))

if check == 1:
    user.createacc()

if check == 2:
    user.deposit()

if check == 3:
    user.withdraw()

if check == 4:
    user.details()

if check == 5:
    user.update1()

if check == 6:
    user.delete()