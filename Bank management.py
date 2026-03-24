
        
print("------------ BANK MANAGEMENT SYSTEM -------------")

class Account:
    def __init__(self, name, accno, balance, pin):
        self.name = name
        self.accno = accno
        self.balance = balance
        self.pin = pin


class BankManagement:
    def __init__(self):
        self.bank = []

    def create_account(self):
        name = input("Enter name: ")
        acc_no = input("Enter account number: ")

        # Check duplicate account
        for acc in self.bank:
            if acc.accno == acc_no:
                print("Account already exists!")
                return
        while True:
            try:
                balance = int(input("Enter balance: "))
                if balance >= 0:
                    break
                else:
                    print("Balance cannot be negative")
            except ValueError:
                print("Invalid input")
        while True:
            pin = input("Enter 4-digit PIN: ")
            if pin.isdigit() and len(pin) == 4:
                pin = int(pin)
                break
            else:
                print("Invalid PIN! Try again")

        acc = Account(name, acc_no, balance, pin)
        self.bank.append(acc)
        print("Account created successfully!")

    
    def view_account(self):
        acc_no = input("Enter account number: ")
        for acc in self.bank:
            if acc.accno == acc_no:
                print("Name:", acc.name)
                print("Account Number:", acc.accno)
                print("Balance:", acc.balance)
                return
        print("Account not found")
    def search_account(self):
        acc_no = input("Enter account number: ")
        for acc in self.bank:
            if acc.accno == acc_no:
                print("Account exists")
                print("Name:", acc.name)
                print("Balance:", acc.balance)
                return
        print("Account not found")
    def deposit(self):
        acc_no = input("Enter account number: ")
        for acc in self.bank:
            if acc.accno == acc_no:
                amount = input("Enter amount to deposit: ")
                if amount.isdigit() and int(amount) > 0:
                    amount = int(amount)
                    acc.balance += amount
                    print("Amount deposited successfully")
                    print("New Balance:", acc.balance)
                    return
                else:
                    print("Invalid amount")
                    return
        print("Account not found")
    def withdraw(self):
        acc_no = input("Enter account number: ")
        for acc in self.bank:
            if acc.accno == acc_no:
                amount = input("Enter amount to withdraw: ")
                if amount.isdigit() and int(amount) > 0:
                    amount = int(amount)
                    if amount <= acc.balance:
                        acc.balance -= amount
                        print("Withdrawal successful")
                        print("Remaining Balance:", acc.balance)
                    else:
                        print("Insufficient balance")
                    return
                else:
                    print("Invalid amount")
                    return
        print("Account not found")
    def check_balance(self):
        acc_no = input("Enter account number: ")
        for acc in self.bank:
            if acc.accno == acc_no:
                print("Balance:", acc.balance)
                return
        print("Account not found")

bank = BankManagement()

while True:
    print("\n--------- MENU ---------")
    print("1. Create Account")
    print("2. View Account")
    print("3. Search Account")
    print("4. Withdraw")
    print("5. Deposit")
    print("6. Check Balance")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.view_account()
    elif choice == "3":
        bank.search_account()
    elif choice == "4":
        bank.withdraw()
    elif choice == "5":
        bank.deposit()
    elif choice == "6":
        bank.check_balance()
    elif choice == "7":
        print("Exiting...")
        break
    else:
        print("Invalid choice")        
    
         
        
        
        
      
