#start

users = {}
status = ""

def displayMenu():
    print('Hi Welcome to Diet Nutrition app')
    status = input("Do you already have an account? yes/no? Press q to quit: ")
    if status == "yes":
        oldUser()
    elif status == "no":
        newUser()
    elif status == "q":
        exit()

def newUser():
    print("Hi welcome pls create a new profile")
    createLogin = input("Create login name: ")

    if createLogin in users:
        print("\nLogin profile already exist!\n")
    else:
        createPass = input("Create password: ")
        users[createLogin] = createPass
        print("\nUser created!\n")
        BMI()

def oldUser():
    print("Hi welcome back pls enter your existing account")
    login = input("Enter login name: ")
    password = input("Enter password: ")

    if login in users and users[login] == password:
        print("\nLogin successful!!!\n")
        BMI()
    else:
        print("\nUser doesn't exist pls try again!\n")
        


def BMI():  
    print("Hi welcome back pls enter your existing account")
    login = input("Enter login name: ")
    password = input("Enter password: ")
    if login in users and users[login] == password:
        print("\nLogin successful!!!\n")
    else:
        print("\nUser doesn't exist pls try again!\n")
        exit()
        
    height=float(input("Enter your height in inches: "))
    weight=float(input("Enter your Weight in lbs: "))
 
    BMI=weight/(height**2) * 703
    print("BMI Calculated is:  ",BMI)
 
    if(BMI>0):
        if(BMI<=16):
            print("You are very underweight")
        elif(BMI<=18.5):
            print("You are underweight")
        elif(BMI<=25):
            print("You are Healthy Congrats!")
        elif(BMI<=30):
            print("You are overweight")
        else: 
            print("You are very overweight")
    else:
        print("Invalid details")




while status != "q":
    displayMenu()


