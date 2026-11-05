#Banking System
#Classes: customer, account, SavingsAccount, checking account
#Features system features: deposits, withdrawls, transfers, account balances, transaction history, validation
#class setup: Account(Parent class) attributes are - balance,account_number, transaction_histroy, owner(CUSTOMER OBJECT -COMPOSITION)
#account methods: deposit, withdrawawl, transfer(amount, to_account), get_balance , show_hisotry
#class set up: child classes - savings account(attributes:interest_sate/ Method: add_interest )
#class set up: child classes - Checking account(attributes: overdraft_limit + its own account behaivor)



class Customer:
    def __init__(self,name, username, password):
        self.name = name
        self.username = username
        self.__password = password

        
    def get_password(self):
        return self.__password

    def validate_login(self, password, username):
            if self.__password == password and self.username == username:
                print(f"Login Succesfull, welcome {self.name}!")
                return True
            else:
                print("Incorrect Password, please try again")
                return False


class Account:
    def __init__(self, account_number, balance, owner):
        self.account_number = account_number
        self.balance = balance
        self.owner = owner
        self.transaction_hisotry = []


    def deposit(self, amount):
         if amount > 0:
            self.balance += amount
            print(f"Deposit of {amount} was succesfull")
         else:
             print("Cannot deposit anyhting less than 0")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Your withdrawal of {amount} was succesful")
        else:
            print("Insufficient funds")

    def transfer(self, ammount, to_account):
        self.withdrawal(ammount)
        to_account.deposit(ammount)
        print("Your Transfer of funds was succesfull!")

    def get_balance(self):
        print(f"Your current balance is: {self.balance}")

    def show_history(self):
        for item in self.transaction_hisotry:
            print(item)
            
class SavingsAccount(Account):
    def __init__(self, account_number, balance, owner, interest_rate):
        super().__init__(account_number, balance, owner)
        self.interest_rate = interest_rate

    def add_interest(self, rate):
        if rate > 0:
            self.interest_rate += rate
            print(f"You're all set {self.owner} ,  our new intertest rate is {self.interest_rate} !")
        else:
            print("Unable to add a negative interest rate!")

class CheckingAccount(Account):
    def __init__(self, account_number, balance, owner, overdraft_limit=500):
        super().__init__(account_number, balance, owner)
        self.overdraft_limit = overdraft_limit

    def change_limit(self, new_limit):
        if 0 <= new_limit <= 1000:
            self.overdraft_limit = new_limit
            print(f"Congradulations {self.owner} your new overdraft limit is {self.overdraft_limit} !")
        else:
            print("Print that limit is outside of the acceptable range!")


c1 = Customer("Michael", "MichaelTMurchie", "Burrito697")
savings  = SavingsAccount(1001, 1000, c1, 0.02)
checking = CheckingAccount(1002, 500, c1)


def get_account(which):
    which = which.lower()
    if which in ["savings", "saving"]:
        return savings
    elif which in ["checking", "check"]:
        return checking
    else:
        return None


def main():
    print("\n" + "=" * 50)
    print("             Banking System")
    print("=" * 50)

    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if not c1.validate_login(username, password):
        return


    while True:

        print("="*50)
        print("1. Deposit")
        print("2. Withdrawl")
        print("3. Transfer")
        print("4. View Balances")
        print("5. Transaction History")
        print("6. Exit")
        print("="*50)

        choice = print("Please choose an option(1-6) ")

        if choice == "1":
           
           acct = get_account(input("Which account? (savings/checking): "))
           if acct:
                amount = float(input("How much? "))
                acct.deposit(amount)
           else:
                print("Account not recognized.")

        elif choice == "2":
            acct = get_account(input("Which account? (savings/checking): "))
            if acct:
                amount = float(input("How much? "))
                acct.withdrawal(amount)
            else:
                print("Account not recognized.")

        elif choice == "3":
            from_account = input("Transfer FROM which account? (savings/checking): ").lower()
            if from_account in ["savings", "saving"]:
                amount = float(input("How much? "))
                savings.transfer(amount, checking)
            elif from_account in ["checking", "check"]:
                amount = float(input("How much? "))
                checking.transfer(amount, savings)
            else:
                print("Account not recognized.")

        elif choice == "4":
            acct = get_account(input("Which account? (savings/checking): "))
            if acct:
                acct.get_balance()
            else:
                print("Account not recognized.")

        elif choice == "5":
            acct = get_account(input("Which account? (savings/checking): "))
            if acct:
                acct.show_history()
            else:
                print("Account not recognized.")

        elif choice == "6":
            print("Thanks for banking with us!")
            break

        else:
            print("Please pick a valid option (1-6).")


if __name__ == "__main__":
    main()



