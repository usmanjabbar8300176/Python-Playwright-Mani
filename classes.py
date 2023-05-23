"""
Write a Python class called BankAccount that has the following attributes:

  balance: The current balance of the account
  interest_rate: The annual interest rate of the account
The class should have the following methods:

  deposit(amount): Deposits an amount into the account
  withdraw(amount): Withdraws an amount from the account
  calculate_interest(): Calculates the interest earned on the account for the current year
  print_statement(): Prints a statement showing the current balance of the account and the interest earned for the current year

"""

class  BankAccount:
    #Constructor         1000     0.5
    def __init__ (self, balance,Interest_rate, Account_Name):
        # balance
        #1000             10000
        self.balance  = balance
        self.Interest_rate = Interest_rate
        self.Account_Name = Account_Name
        
        #4 Method
    def deposit(self, amount):
        self.balance += amount
        # self.balance = self.balance + amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("NOT ENOUGH AMOUNT")
        self.balance -= amount
      #  self.balance = self.balance - amount

    def calculate_interest(self):
        # interest = self.balance/self.Interest_rate * 100
        interest = self.balance * self.Interest_rate / 100
        return interest
        
    def print_statement(self):
        print("Account Name:", self.Account_Name)
        print("Current balance: $", self.balance)
        print("Interest earned for the current year: $", self.calculate_interest())

# account = BankAccount(1000, 0.06, "Usman")
# accountHamza = BankAccount(40, 0.8, "Hamza")
# accountMani = BankAccount(500, 0.5, "Mani")

# accountHamza.deposit(300)
# accountHamza.print_statement()

# accountMani.withdraw(200)
# accountMani.print_statement()

# account.withdraw(700)
# account.print_statement()

# account = BankAccount(1000, 0.5)
# account.deposit(300)