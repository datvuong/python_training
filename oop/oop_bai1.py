import json

class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_name = account_name
        self._account_number = account_number
        self.set_balance(balance)

    def get_account_name(self):
        return self._account_name
    
    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
    
    def display(self):
        print(
            f"Account Name: {self.get_account_name()}\n", 
            f"Account Number:{self.get_account_number()}\n",
            f"Account Balance:{self.get_balance()}\n")

    def withdraw(self, amount):
        if self.get_balance() >= amount and amount > 0:
            self.set_balance(self.get_balance() - amount)
        else:
            print("Can't withdraw, balance is not sufficent.")
        self.display()
    
    def deposit(self, amount):
        if amount > 0:
            self.set_balance(self.get_balance() + amount)
        else:
            print("Deposit amount is not valid.")
        self.display()

if __name__ == '__main__':
    me = BankAccount('1234','3xere')
    me.deposit(100)
    me.withdraw(10)
