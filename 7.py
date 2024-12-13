class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")
    def get_balance(self):
        return self._balance
class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.03):
        super().__init__(balance)  
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self._balance * self.interest_rate
        return interest
    def apply_interest(self):
        interest = self.calculate_interest()
        self._balance += interest
        print(f"Interest applied: ${interest}. New balance: ${self._balance}")
account = BankAccount(1000)
account.deposit(500)
savings_account = SavingsAccount(1000, 0.05)
savings_account.deposit(200)
interest = savings_account.calculate_interest()
print(f"Calculated interest: ${interest}")
savings_account.apply_interest()
print(f"Final balance: ${savings_account.get_balance()}")
