class BankAccount:
    def __init__(self,account_balance=0):
        self.account_balance = account_balance
    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")
    
# my_account = BankAccount()
# print("Initial Balance:", my_account.display_balance())
# my_account.deposit(50)
# print("Balance after deposit of $50:", my_account.display_balance())
# my_account.withdraw(20)
# print("Balance after withdrawal of $20:", my_account.display_balance())
# my_account.withdraw(150)  # Attempt to withdraw  with insufficient funds
# print("Balance after attempting to withdraw $150:", my_account.display_balance())
# print("Current Balance:", my_account.display_balance())