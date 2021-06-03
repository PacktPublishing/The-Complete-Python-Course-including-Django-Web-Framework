# Banking App
# Class Based
# Withdrawal and Deposit
# Write the transaction to a python file
# while True:
# input
# classes
# open()
# method
# properties

class Bank:

    def __init__(self, initial_amount=0.00):
        self.balance = initial_amount

    def log_transaction(self, transaction_string):
        with open("transactions.txt", "a") as file:
            file.write(f"{transaction_string} \t\t\tBalance: {self.balance}\n")

    def withdrawal(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance - amount
            self.log_transaction(f"Withdrew {amount}")

    def deposit(self, amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.log_transaction(f"Deposited {amount}")

account = Bank(50.50)
while True:
    try:
        action = input("What kind of action do you want to take? ")
    except KeyboardInterrupt:
        print("\nLeaving the ATM\n")
        break

    if action in ["withdrawal", "deposit"]:
        if action == "withdrawal":
            amount = input("How much do you want to take out? ")
            account.withdrawal(amount)
        else:
            amount = input("How much do you want to put in? ")
            account.deposit(amount)

        print("Your balance is", account.balance)
    else:
        print("That is not a valid action. Try again.")
