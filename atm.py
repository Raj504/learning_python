class Atm:

    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    def menu(self):
        user_input  = input("""
        Hello, how you want to proceed?
        1. create pin
        2. deposit
        3. withdraw
        4. check balance
        """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print("invalid input")

    def create_pin(self):
        self.pin = input("enter your pin")
        print("pin set successfully")
 
    def deposit(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))  
            self.balance = self.balance + amount
            print("deposit successfull")
        else : 
            print("invalid pin")

    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount")) 
            if amount<self.balance:
                self.balance = self.balance - amount
                print("operation seccessfull")
            else: 
                print("insufficent balance")
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else: 
            print("invalid pin")


