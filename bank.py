class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        return f"{self.name.title()}, {self.age}"

class Account(User):
    total_deposits = 0
    total_withdrawals = 0

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance
    
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


print('Welcome to ABC Bank')
name = input('What is your name? ')
age = int(input('What is your age? '))
deposit = float(input('How much do you have to start? '))
while True:
    account_type = input('What type of account do you want to create? Enter S for savings, C for checking: ').upper()
    if account_type == 'S':
        user = Savings(name, age, deposit)
        break
    elif account_type == 'C':
        user = Checking(name, age, deposit)
        break
    else:
        print('Invalid input. Please enter S or C')

while True:
    print(f"""
        Welcome to ABC Bank {name, age}
        1. Check account balance
        2. Deposit
        3. Withdraw
        4. End
    """)
    user_input = input('> ')
    if user_input == '1':
        print(f"Your current balance is ${user.balance}")
    elif user_input == '2':
        print(user.deposit())
    elif user_input == '3':
        print(user.withdraw())
    elif user_input == '4':
        break
    else:
        print('Please enter a number between 1-4')