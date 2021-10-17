import json

class BankAccount:
    bank_accounts = []
    def __init__(self, account_number, account_name, balance=0):
        self._account_name = account_name
        self._account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"| {self.account_number:13} | {self.account_name:23} | {self.balance:>13} |"

    @property
    def account_name(self):
        return self._account_name
    
    @property
    def account_number(self):
        return self._account_number
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self._balance = new_balance
    
    @classmethod
    def from_csv(cls, file_path):
        with open(file_path, 'r') as f:
            for record in f:
                account_number, account_name, balance = record.split(',')
                cls.bank_accounts.append(cls(account_number, account_name, int(balance)))
        return cls.bank_accounts

    @classmethod
    def from_json(cls, file_path):
        list_input = json.load(open(file_path))
        for r in list_input:
            cls.bank_accounts.append(cls(**r))
        return cls.bank_accounts

    def display(self):
        print(
            f"""Account Name: {self.account_name}\nAccount Number:{self.account_number}\nAccount Balance:{self.balance}""")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Can't withdraw, balance is not sufficent.")
        self.display()
    
    def deposit(self, amount):
        self.balance += amount
        self.display()

if __name__ == '__main__':
    me = BankAccount('1234','3xere')
    me.account_number

    BankAccount.from_json('bank_account.json')
    BankAccount.from_csv('bank_account.csv')
    me.deposit(100)
    me.withdraw(10)
    print(f"| {'Number':13} | {'Account Name':23} | {'Balance':13} |")
    print(f"|{'-' * 15}|{'-' * 25}|{'-' * 15}|")
    for account in BankAccount.bank_accounts:
        print(account)
