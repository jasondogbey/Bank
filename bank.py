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
        dp = float(input('How much would you like to deposit? '))
        self.balance += dp
        self.total_deposits += 1
        return f"Deposit successful!! The balance is now ${self.balance}"
    
    def withdraw(self):
        wd = float(input('How much do you want to withdraw? '))
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
        wd = float(input('How much do you want to withdraw? '))
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
        wd = float(input('How much do you want to withdraw? '))
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

user1 = Checking('capi', 30, 50)
print(user1.show_details(), 'welcome')
print(user1.withdraw())
print(user1.withdraw())