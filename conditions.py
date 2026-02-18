email = input("Enter your email: ")
if '@' in email:
    password  = input("Enter your password: ")

    if email == "rajaryanz.dev@gmail.com" and password == "123456":
        print("you're welcome")
    elif email == "rajaryanz.dev@gmail.com" and password != "123456":
        print("password incorrect")
        password  = input("Enter your password: ")
        if password == "123456":
            print("finally correct")
        else:
            print("still incorrect")
    else:
        print("incorrect credentials")
else:
    print("wrong format of email")