# bank account example program
# class BankAccount:
#   bank_name = "MahaPurush Bank"
#   total_accounts = 0
#   all_account_numbers = {}

#   def __init__(self, account_holder,account_number, balance = 0):
#     self.account_holder = account_holder
#     self.balance = balance
#     self.account_number = account_number
#     BankAccount.total_accounts += 1
#     BankAccount.all_account_numbers[self.account_number] = self.account_holder

#   def deposit(self):
#     amount = int(input("Enter an amount to deposit: "))
#     self.balance = self.balance + amount

#   def withdraw(self):
#     amount = int(input("Enter an amount to withdraw: "))
#     self.balance = self.balance - amount

#   def display_account(self):
#     print("Account Details: ")
#     print(f"Account Holder:\t{self.account_holder}")
#     print(f"Account Number:\t{self.account_number}")
#     print(f"Account Balance:\t{self.balance}")

#   @classmethod
#   def display_Bank_Details(cls):
#     print("Bank Details: ")
#     print(f"Bank Name:\t{BankAccount.bank_name}")
#     print(f"Number of Accounts:\t{BankAccount.total_accounts}")
#     print(f"Accounts:\t{BankAccount.all_account_numbers}")


# print("//////////////////WELCOME TO MAHAPURUSH BANK//////////////////")

# account_holder,account_number = input("Enter: \ni.) " \
# "The name of the Account Holder\nii.) Account Number\n"
# "[account holder,accountnumber]").split(",")

# account = BankAccount(account_holder=account_holder, account_number= account_number)

# print("Which operation would you like to perform: ")
# option = int(input("1.)Deposit\n2.)Withdraw\n"\
#                    "3.)Display Account Details\n"))

# match option:
#   case 1:
#     account.deposit()

#   case 2:
#     account.withdraw()
  
#   case 3:
#     account.display_account()

#   case _:
#     print("Please enter a valid operation.")

# /////////////////////////////////////////