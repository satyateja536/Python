import random
class Bank:
    bankDB = {} #Declaring dictionary to hold key=account number and value = list of name and balance
    def __intit__(self):
        self.bankDB = {} #dictionary would look like {25200:['Customer1',500],34500:['Customer2',400]}
    def check_account(self,name,account_no): # To validate the existing customer against the dictionary
        status = False
        if account_no in self.bankDB.keys(): #checking for account no in dictionary
            self.customer = self.bankDB.get(account_no)
            if self.customer[0] == name: #comparing the input name to existing name
                status = True # Customer exists in the Dictionary
            else:
                status = False # Customer Doesn't exist in the dictionary
        else:
            status = False
        return status
    def create_account(self,name,deposit): # Method to create a new customer
        self.account_no = random.randint(10000,99999)
        self.bankDB[self.account_no] = [name,deposit]
        return self.account_no
    def deposit_money(self,account_no,amount): # Method to deposit money based on key: account_no
        self.customer = self.bankDB.get(account_no)
        if amount > 0:
            total_amount = self.customer[1] + amount
            self.customer[1] = total_amount # modified amount is added to the list value balance
            self.bankDB[account_no] = self.customer
            self.request_balance(account_no)
        else:
            print("Amount must be greater than 0")
    def withdraw_money(self,account_no,amount): # Method to Withdraw money based on key: account_no
        self.customer = self.bankDB.get(account_no)
        if self.customer[1] > amount:
            total_amount = self.customer[1] - amount
            self.customer[1] = total_amount # modified amount is added to the list value balance
            self.bankDB[account_no] = self.customer
            self.request_balance(account_no)
        else:
            print("Insufficient balance: {}".format(self.customer[1]))
    def request_balance(self,account_no): # Method to print the balance of the account
        self.account_no = account_no
        self.customer = self.bankDB.get(self.account_no)
        print("Balance in the account with no: {}  is: {}".format(self.account_no,self.customer[1]))


bank = Bank()
while True:
    print("Enter your choice: 1. Open New Account 2. Deposit Money 3. Withdraw Money 4. Check Balance 5. Exit" )
    choice = int(input())
    if choice == 1:
        print("Enter Name of the account holder: ")
        name = input()
        print("Enter deposit amount: ")
        deposit = int(input())
        account_no = bank.create_account(name,deposit)
        print("Bank Account Created with account_no: {} and use this no for future transactions".format(account_no))
    elif choice == 2:
        print("Enter account no: ")
        account_no = int(input())
        print("Enter name: ")
        name = input()
        status = bank.check_account(name,account_no)
        if status == True:
            print("Enter deposit amount: ")
            amount = int(input())
            bank.deposit_money(account_no,amount)
            print("Amount Deposited Successfully")
        else:
            print("Account doesn't exit with given name and account no. Please check you details")
    elif choice == 3:
        print("Enter account no: ")
        account_no = int(input())
        print("Enter name: ")
        name = input()
        status = bank.check_account(name,account_no)
        if status == True:
            print("Enter Withdrawl amount: ")
            amount = int(input())
            bank.withdraw_money(account_no,amount)
            print("Amount Withdrawn Successfully")
        else:
            print("Account doesn't exit with given name and account no. Please check you details")
    elif choice == 4:
        print("Enter account no: ")
        account_no = int(input())
        print("Enter name: ")
        name = input()
        status = bank.check_account(name,account_no)
        if status == True:
            bank.request_balance(account_no)
        else:
            print("Invalid Account Details")
    else:
        quit()
