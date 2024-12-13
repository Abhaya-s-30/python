class bankaccount:
    def __init__(self,acc_num,balance):
        self.acc_num=acc_num
        self.balance=balance
    def calculate_interest(self):
        raise NotImplementedError("Subclasses must override this method")
class savingsaccount(bankaccount):
    def calculate_interest(self):
        return self.balance * 0.03
class fixeddepositaccount(bankaccount):
    def calculate_interest(self):
        return self.balance * 0.06
accounts = [
    savingsaccount("SA123", 1000),
    fixeddepositaccount("FD456", 5000)
]
for account in accounts:
    print(f"Account Number: {account.acc_num}")
    print(f"Balance: {account.balance}")
    print(f"Interest: {account.calculate_interest()}")