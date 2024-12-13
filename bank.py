class bankaccount:
    def __init__(self,account_number,balance):
        self.account_number=account_number
        self.balance=balance
    def display_account_details(self):
        print(f"account number:{self.account_number}")
        print(f"balance: rs{self.balance}")
class savingsaccount(bankaccount):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate=interest_rate
    def calculate_interest(self):
        return self.balance*(self.interest_rate/100)
class fixeddepositaccount(savingsaccount):
    def __init__(self,account_number,balance,interest_rate,duration):
        super().__init__(account_number,balance,interest_rate)
        self.duration=duration
    def calculate_total_interest(self):
        total_interest=self.calculate_interest()*self.duration
        return total_interest
    def display_account_details(self):
        super().display_account_details()
        print(f"interest rate: {self.interest_rate}%")
        print(f"duration:{self.duration} years")
        print(f"total interest earned:rs{self.calculate_total_interest()} ")
account_number=input("enter account number:")
balance=float(input("enter balance:"))
interest_rate=float(input("enter interest rate:"))
duration=int(input("enter duration(in years):"))
fd_account=fixeddepositaccount(account_number,balance,interest_rate,duration)
fd_account.display_account_details()