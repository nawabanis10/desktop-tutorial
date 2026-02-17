user={}

def signup():
    user_name=input("enter new user name")
    if user_name in user:
        print("user name is already exsit")
        return
    password=input("enter password")
    user[user_name]=password
    print(f'user{user_name} signup successfuly')

def signin():
    user_name=input("enter your name")
    password=input("enter your passwrod")
    if user_name in user and user[user_name]==password:
        print(f'wellcome back{user_name}')
    else:
        print("invalid user_name or password !")
    
while True:
    print("===Main Menu===")
    print("1.sign_up")
    print("2.sign_in")
    print("3.Exit")

    choice=input("enter your choice: ")
    match choice:
        case "1":
            signup()
        case "2":
            signin()
        case "3":
            print("Exiting program ")
            break
        case _:
            print("invalid choice please select 1,2 or 3")