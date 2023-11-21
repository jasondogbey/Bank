# Define a User class representing bank customers
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Return formatted user details
    def show_details(self):
        return f"{self.name.title()}, {self.age} years old"

# Define an Account class as a base class for bank accounts
class Account(User):
    total_deposits = 0
    total_withdrawals = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
    
    # Method to deposit money into the account
    def deposit(self):
        try:
            dp = float(input('How much would you like to deposit? '))
        except ValueError:
            return "Please enter a valid amount."
        
        if dp <= 0:
            return "Invalid amount. Deposit amount should be a positive number."
        
        self.balance += dp
        self.total_deposits += 1
        return f"Deposit successful!! The balance is now ${self.balance}"
    
    def withdraw(self):
        try:
            wd = float(input('How much do you want to withdraw? '))
        except ValueError:
            return "Please enter a valid amount."
        
        if wd <= 0:
            return "Invalid amount. Withdrawal amount should be a positive number."
        
        if wd > self.balance:
            return f"You do not have enough money to withdraw ${wd}, your balance is ${self.balance}"
        self.balance -= wd
        self.total_withdrawals += 1
        return f"${wd} withdrawn! Your current balance is ${self.balance} "

class Savings(Account):
    interest_rate = 0.04
    max_withdrawals_per_month = 3
    withdrawals_this_month = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age, balance)
    
    def calculate_interest_rate(self):
        interest = self.interest_rate * self.balance
        self.balance += interest
        return f"Interest added! Your current balance is ${self.balance}"
    
    def withdraw(self):
        try:
            wd = float(input('How much do you want to withdraw? '))
        except ValueError:
            return "Please enter a valid amount."
        
        if wd <= 0:
            return "Invalid amount. Withdrawal amount should be a positive number."
        
        if self.withdrawals_this_month >= self.max_withdrawals_per_month:
            return f"You have reached your maximum number of withdrawals for the month."
        if wd > self.balance:
            return f"You do not have enough money to withdraw ${wd}, your balance is ${self.balance}"
        self.balance -= wd
        self.withdrawals_this_month += 1
        self.total_withdrawals += 1
        return f"${wd} withdrawn! Your current balance is ${self.balance}"

class Checking(Account):
    overdraft_limit = -1000
    overdraft_fee = 30

    def __init__(self, name, age, balance):
        super().__init__(name, age, balance)
    
    def withdraw(self):
        try:
            wd = float(input('How much do you want to withdraw? '))
        except ValueError:
            return "Please enter a valid amount."
        
        if wd <= 0:
            return "Invalid amount. Withdrawal amount should be a positive number."
        
        if wd > (self.balance + abs(self.overdraft_limit)):
            return f"You have exceeded your overdraft limit. Your current balance is ${self.balance} and your overdraft limit is ${self.overdraft_limit}"
        if wd > self.balance:
            self.balance -= wd
            self.balance -= self.overdraft_fee
            self.total_withdrawals += 1
            return f"${wd} withdrawn with overdraft fee of ${self.overdraft_fee}. Your current balance is ${self.balance}"
        self.balance -= wd
        self.total_withdrawals += 1
        return f"${wd} withdrawn! Your current balance is ${self.balance}"

# Create an account based on the provided account type
def create_account(account_type, name, age, deposit):
    if account_type == 'S':
        return Savings(name, age, deposit)
    elif account_type == 'C':
        return Checking(name, age, deposit)
    else:
        return None

# Function to display account details
def display_accounts(accounts):
    for idx, account in enumerate(accounts, start=1):
        print(f"{idx}. {type(account).__name__} - Balance: ${account.balance}")

# Main function to handle user interactions, account creation, and operations
def manage_accounts():
    accounts = []  # List to store created accounts

    print('Welcome to ABC Bank')
    name = input('What is your name? ')
    age = int(input('What is your age? '))

    while True:
        deposit = float(input('How much do you have to start? '))
        account_type = input('What type of account do you want to create? Enter S for savings, C for checking: ').upper()

        user_account = create_account(account_type, name, age, deposit)
        if user_account:
            accounts.append(user_account)
        else:
            print('Invalid input. Please enter S or C.')

        while True:
            print(f"""
                Welcome to ABC Bank {name, age}
                1. Check account balance
                2. Deposit
                3. Withdraw
                4. Switch account
                5. End
                6. Create another account
            """)
            user_input = input('> ')
            if user_input == '1':
                display_accounts(accounts)
            elif user_input == '2':
                print(user_account.deposit())
            elif user_input == '3':
                print(user_account.withdraw())
            elif user_input == '4':
                print("Available accounts:")
                display_accounts(accounts)
                account_choice = int(input("Enter the account number to switch: "))
                if 0 < account_choice <= len(accounts):
                    user_account = accounts[account_choice - 1]
                else:
                    print("Invalid account number.")
            elif user_input == '5':
                exit()  # Exit the program
            elif user_input == '6':
                break  # Create another account
            else:
                print('Please enter a number between 1-6')

# Run the program by calling the main function
manage_accounts()