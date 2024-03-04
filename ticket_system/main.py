"""Ticket purchasing and checking program"""

 # from now on Ticket_manager will be referred to as tm

from abc import ABC
import pickle
import time

class Ticket():
    type = None
    price = None
    destination = None

class User(ABC):
    personal_tickets = None
    def __init__(self) -> None:
        self.first_name = input("Enter your first name:")
        time.sleep(.4)
        self.last_name = input("Enter your last name:")
        time.sleep(.4)
        self.password = input("Enter your password:")
        time.sleep(.4)
        self.check_password()
        time.sleep(.4)
        self.email = input("Enter your email address:")
        time.sleep(.4)
    
    def check_password(self):
        while True:
            if self.password == input("Enter your password again:"):
                print("Password accepted! Don't forget it.")
                break
            else:
                self.password = input("Enter your password:")

class Regular(User):
    admin_clearance = False

class Admin(User):
    admin_clearance = True


class Ticket_manager:
    regular_users = []
    admin_users = []
    availabe_tickets = []
    current_user = None
    close_program = False
    spacer = 120

    def __init__(self) -> None:
        self.initialize_stored_tm()
        time.sleep(1)
        self.instructions()
        self.options()
        self.logout()
        self.store_tm()

    def store_tm(self):
        with open("tm_data.pkl", "wb") as w_file: # open tm previously stored data or create storage file
            pickle.dump(self, w_file) # store self

    def initialize_stored_tm(self):
        try: # try to open stored tm
            with open("tm_data.pkl", "rb") as r_file:
                data = pickle.load(r_file)
                self.regular_users = data.regular_users
                self.admin_users = data.admin_users
                self.availabe_tickets = data.availabe_tickets
        except: # if on stored tm is found a new one will be created
            print("No previous Ticket manager found.")
            self.store_tm()
            print("A new Ticket manager was created.")
            print("A new admin account will need to be created.")
            self.create_admin()

    def instructions(self):
        print("Hello!") 
        time.sleep(.5)
        print("Welcome to the ticket manager.")
        time.sleep(.5)
        print("This is an automated ticket system.")
        time.sleep(.5)
        print("\nWarning: the changes made during each session are only saved after using the options menu to close the file")
        time.sleep(2.5)
        print("="*self.spacer)
        time.sleep(.4)
    
    def options(self):
        while not self.close_program:
            try:
                if self.current_user.admin_clearance == "admin":
                    print("Welcome Admin")
                    print("-1: Create admin account")
            except:
                pass

            print("What would you like to do?")
            time.sleep(.4)
            print("0: Close program")
            time.sleep(.4)
            print("1: Create accout")
            time.sleep(.4)
            print("2: Log in")
            time.sleep(.4)
            print("3: Log out")
            time.sleep(.4)
            print("4: Buy ticket")
            time.sleep(.4)
            print("5: Verify ticket")
            time.sleep(.4)
            print("6: Check current account")
            time.sleep(.4)
            print("7: Check all accounts")

            try:
                self.exe_options(int(input("\nPlease enter option number to proceed:")))
                print("="*self.spacer)
            except:
                time.sleep(.6)
                print("\nOption not found!")
                time.sleep(.2)
                print("Please enter valid option number.")
                time.sleep(.6)
                print("="*self.spacer)
        time.sleep(.4)
        print("Closing...")
        time.sleep(1)
        print("Bye!")
    
    def exe_options(self, choice: int):
        print()
        if choice == 0:
            self.close()
        elif choice == 1:
            self.create_regular()
        elif choice == 2:
            self.login()
        elif choice == 3:
            self.logout()
        elif choice == 4:
            self.buy_ticket()
        elif choice == 5:
            self.verify_ticket()
        elif choice == 6:
            self.check_current_account()
        elif choice == 7:
            self.check_accounts()
        else:
            try:
                if self.current_user.admin_clearance == "admin":
                    if choice == -1:
                        self.create_admin
            except:
                time.sleep(.6)
                print("Option not found!")
                time.sleep(.2)
                print("Please enter valid option number.")
                time.sleep(.6)

    def create_admin(self):
        print("This will log you out of your current account.")
        time.sleep(.4)
        if input("Are you sure (yes/no):") == "yes":
            self.current_user = None
            while True:
                time.sleep(.8)
                print("Creating new admin...")
                self.current_user = Admin()
                if not any(obj.first_name == self.current_user.first_name for obj in self.admin_users) or not any(obj.last_name == self.current_user.last_name for obj in self.admin_users):
                    self.admin_users.append(self.current_user)
                    time.sleep(1)
                    print("Done!")
                    break
                else:
                    self.current_user = None
                    print("Account name already taken.")
                    print("Choose a new name and create a new account.")
        print("Account creation aborted.")

    def create_regular(self):
        def create_user():
            while True:
                time.sleep(.8)
                print("Creating new user...")
                self.current_user = Regular()
                if not any(obj.first_name == self.current_user.first_name for obj in self.regular_users) or not any(obj.last_name == self.current_user.last_name for obj in self.regular_users):
                    self.regular_users.append(self.current_user)
                    time.sleep(1)
                    print("Done!")
                    break
                else:
                    self.current_user = None
                    print("\nAccount name already taken.")
                    print("Choose a new name and create a new account.\n")

        if self.current_user != None:
            time.sleep(.4)
            print("This will log you out of your current account")
            if input("Are you sure (yes/no):") == "yes":
                self.current_user = None
                create_user()
        else:
            create_user()
            

    def login(self):
        self.check_accounts()
        print("\n="*self.spacer)
        current_account = self.current_user
        while self.current_user == current_account:
            first_name = input("To select account enter account first name:")
            last_name = input("To select account enter account last name:")
            for account in self.regular_users:
                if account.first_name == first_name and account.last_name == last_name:
                    print("\nAccount found!")
                    while True:
                        if account.password == input("Enter account password:"):
                            self.current_user = account
                            print("Log in successful!")
                            break
                        else:
                            print("Incorrect password.")
                            if input("Would you like to continue (yes/no):") == "no":
                                break
            for account in self.admin_users:
                if account.first_name == first_name and account.last_name == last_name:
                    print("Account found!")
                    while True:
                        if account.password == input("Enter account password:"):
                            self.current_user = account
                            print("Log in successful!")
                            break
                        else:
                            print("Incorrect password.")
                            if input("Would you like to continue (yes/no):") == "no":
                                break


    def logout(self):
        self.current_user = None

    def check_current_account(self):
        if self.current_user != None:
            print("="*self.spacer)
            print("Account information:\n")
            print(f"Name: {self.current_user.first_name} {self.current_user.last_name}")
            print(f"Email address: {self.current_user.email}")
            print(f"Password: {self.current_user.password}")
            print(f"Personal tickets: {self.current_user.personal_tickets}")
        else:
            print("You have no account currently active.")
            print("Please log in or create an account.")

    def check_accounts(self):
            print("Regular accounts:")
            if len(self.regular_users) != 0:
                for account in self.regular_users:
                    print("="*self.spacer)
                    print("Account information:\n")
                    print(f"Name: {account.first_name} {account.last_name}")
                    print(f"Email address: {account.email}")
            else:
                print("No regular accounts found.")
            print("\n\nAdmin accounts:")
            if len(self.admin_users) != 0:
                print("Admin accoutns:")
                for account in self.admin_users:
                    self.check_user(account)
            else:
                print("No admin accounts found.")

    def buy_ticket(self):
        pass

    def verify_ticket(self):
        pass

    def close(self):
        self.logout()
        self.store_tm()
        self.close_program = True
    
    def delete_tm(self):
        with open("tm_data.pkl", "wb") as w_file:
            w_file.write()

        
Ticket_manager()

# Add route system
# Add automatic email
# Tamper proof system
    
# Admin needs to be able to add new tickets
# Admin special login