from random import randint
from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):
    @abstractmethod
    def create_account(self, name, initial_deposit):
        pass

    @abstractmethod
    def user_authentication(self, name, acc_num):
        pass

    @abstractmethod
    def withdrawal(self, acc_num, withdraw_amt):
        pass

    @abstractmethod
    def deposit(self, acc_num, deposit_amt):
        pass

    @abstractmethod
    def show_balance(self, acc_num):
        pass


class SavingsAccount(Account):
    def __init__(self):
        self.account = {}

    def create_account(self, name, initial_deposit):
        account_num = randint(10000, 99999)
        while account_num in self.account:
            account_num = randint(10000, 99999)
        self.account[account_num] = [name, initial_deposit]
        print(f"Account created successfully! Your account number is {account_num}")
        return account_num

    def is_account_valid(self, acc_num, name=None):
        if acc_num not in self.account:
            print("Account not found.")
            return False
        if name and self.account[acc_num][0] != name:
            print("Authentication Failed!")
            return False
        return True

    def user_authentication(self, name, acc_num):
        return self.is_account_valid(acc_num, name)

    def withdrawal(self, acc_num, withdraw_amt):
        if self.is_account_valid(acc_num):
            if withdraw_amt > self.account[acc_num][1]:
                print("Insufficient balance.")
            else:
                self.account[acc_num][1] -= withdraw_amt
                self.show_balance(acc_num)

    def deposit(self, acc_num, deposit_amt):
        if self.is_account_valid(acc_num):
            self.account[acc_num][1] += deposit_amt
            self.show_balance(acc_num)

    def show_balance(self, acc_num):
        if self.is_account_valid(acc_num):
            print(f"Your current balance is: {self.account[acc_num][1]}")


account = SavingsAccount()

while True:
    print("\nSelect an option:")
    print("1. Create a new account.")
    print("2. Access the existing account.")
    print("3. Exit")
    option = input("Enter the option number: ")

    if option == "1":
        name = input("Enter your name: ")
        try:
            initial_deposit = int(input("Enter your initial deposit: "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        account.create_account(name, initial_deposit)

    elif option == "2":
        name = input("Enter your name: ")
        acc_num = int(input("Enter your account number: "))
        authentication_status = account.user_authentication(name, acc_num)

        if authentication_status is True:
            while True:
                print("\nSelect an option:")
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Check Balance")
                print("4. Go back to Home")
                option = input("Enter the option number: ")

                if option == "1":
                    amount = int(input("Enter the withdrawal amount: "))
                    account.withdrawal(acc_num, amount)
                elif option == "2":
                    amount = int(input("Enter the deposit amount: "))
                    account.deposit(acc_num, amount)
                elif option == "3":
                    account.show_balance(acc_num)
                elif option == "4":
                    break
                else:
                    print("Invalid option, please try again.")
    elif option == "3":
        print("Thank you using MyBank!")
        break
    else:
        print("Invalid option, please try again.")
