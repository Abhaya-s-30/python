class pancard:
    def set_pan_details(self,pan_number):
        self.pan_number=pan_number
    def get_pan_details(self):
        return f"pan number: {self.pan_number}"
class aadharcard:
    def set_aadhar_details(self,aadhar_number):
        self.aadhar_number=aadhar_number
    def get_aadhar_details(self):
        return f"aadhar number: {self.aadhar_number}"
class bankaccount(pancard,aadharcard):
    def set_account_details(self,account_number,account_holder_name):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
    def get_account_details(self):
        return f"account holder: {self.account_holder_name}, account_number: {self.aadhar_number}"
    def display_all_details(self):
        print(self.get_account_details())
        print(self.get_pan_details())
        print(self.get_aadhar_details())
account_holder_name=input("enter account holder name: ")
account_number=input("enter account number: ")
pan_number=input("enter pan card number: ")
aadhar_number=input("enter aadhar card number: ")
bank_account=bankaccount()
bank_account.set_account_details(account_number,account_holder_name)
bank_account.set_pan_details(pan_number)
bank_account.set_aadhar_details(aadhar_number)
print("\nbank account details:")
bank_account.display_all_details()