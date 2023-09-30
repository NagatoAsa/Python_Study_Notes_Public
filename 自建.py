while True:
    print("Welcome to the User System")
    nm = str(input("Please enter your user name:"))
    pwd = int(input("Please enter your password:"))
    if nm == "NagatoAsa":
        if pwd == 114514:
            print("Welcome,", nm)
            break
        else:
            print("Password incorrect")
    else:
        print("User doesn't exist")
input("Please press enter to exit")

