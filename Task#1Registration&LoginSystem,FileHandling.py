def register(): #Registration function
    db =open("RegisteredDatabase.txt", "r")
    Username =input("Create username:")
    Password = input("Create password:")
    Password1 = input("Confrim password:")
    u=[]
    p=[]
    for i in db:
        a,b=i.split(", ")
        b=b.strip()
        u.append(a)
        p.append(b)
    data=dict(zip(u,p)) #Created dictionary for username & password
    # print(data)
    emailchar=['@', '.']
    Specialchar = ['$', '@', '#', '%']
    con="@."
    if not any(char in emailchar for char in Username):
        print("Enter valid email address, restart")
        register()
    if Username[0] in emailchar:
        print("Enter valid email address, restart") #It should not start with @, restart
        register()
    if con in Username:
        print("Enter valid email address, restart") #There should not be any . immediate next to @, restart
        register()
    if Username[0] in Specialchar:
        print("Enter valid email address, restart") #Email ID should not start with special character, restart
        register()
    if Username[0].isdigit():
        print("Enter valid email address, restart") #Email ID should not start with numbers, restart
        register()

    if Password != Password1:
        print("Passwords don't not match, restart")
        register()
    if len(Password)<5:
        print("Password length should be not be greater than 4, restart")
        register()
    if len(Password)>16:
        print("length should be lesser than 16, restart")
        register()
    if not any(char.isdigit() for char in Password):
        print('Password should have at least one numeral, restart')
        register()
    if not any(char.isupper() for char in Password):
        print('Password should have at least one uppercase letter, restart')
        register()
    if not any(char.islower() for char in Password):
        print('Password should have at least one lowercase letter, restart')
        register()
    if not any(char in Specialchar for char in Password):
        print('Password should have at least one of the symbols $@#%, restart')
        register()
    elif Username in u:
        print("username exists")
        register()
    else:
        db = open("RegisteredDatabase.txt", "a")
        db.write(Username + ", " + Password + "\n")
        print("Success!")

def access(): #Login function for existing user
    db = open("RegisteredDatabase.txt", "r")
    Username = input("Enter your username:")
    Password = input("Enter your password:")

    if not len(Username or Password)<1:
        u = []
        p = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            u.append(a)
            p.append(b)
        data = dict(zip(u, p))

        try:
            if data[Username]:
                try:
                    if Password==data[Username]:
                        print("Login success")
                        print("Hi", Username)
                    else:
                        print("Password or Username incorrect")
                except:
                    print("Incorrect Password or Username")
            else:
                print("Username or Password doesn't exist")
        except:
            print("Username does't exist Registeration required")
    else:
        print("Please enter the value")

def forget(): #Forget function to retrieve password
    db = open("RegisteredDatabase.txt", "r")
    Username = input("Enter your username:")
    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))

    if Username in u:
        print(f"Your account Password is: {data[Username]}")
    else:
        print("Username doesn't exist, Registeration required")

def home(option=None): #Fuction for option to choose in an interface
    option=input("Login | Signup | Forget Password:")
    if option == "Signup":
        register()
    elif option== "Login":
        access()
    elif option== "Forget Password":
        forget()
    else:
        print("Please enter a valid option")
home()
