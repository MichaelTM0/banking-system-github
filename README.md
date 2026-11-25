# Banking System

A command-line banking application built in Python using object-oriented programming. It supports customer login, separate savings and checking accounts, and the core operations of a real bank — deposits, withdrawals, transfers between accounts, balance checks, and a running transaction history.

This project was built to practice OOP fundamentals: **inheritance**, **composition**, and **encapsulation**.

## Features

* **Secure login** — a customer logs in with a username and password before any account access
* **Two account types** — Savings (with an interest rate) and Checking (with an overdraft limit)
* **Deposits and withdrawals** with validation (no negative deposits, no overdrawing past the balance)
* **Transfers** between the customer's own accounts
* **Balance checks** for any account
* **Transaction history** — every deposit, withdrawal, and transfer is recorded and can be viewed
* **Menu-driven interface** that loops until the user exits

## Requirements

* Python 3.6 or newer
* No external packages — uses only the Python standard library

## Getting Started

1. Clone the repository (update the URL with your own if the repo name differs):

   ```bash
   git clone https://github.com/MichaelTM0/banking-system.git
   cd banking-system
   ```

2. Run the program:

   ```bash
   python bankingsystem.py
   ```

3. Log in with the demo credentials (username `MichaelTMurchie`, password `Burrito697`) and choose an option from the menu.

## Usage

```
==================================================
             Banking System
==================================================
1. Deposit
2. Withdraw
3. Transfer
4. View Balance
5. Transaction History
6. Exit
==================================================
Please choose an option (1-6):
```

## How It Works

The program is organized around four classes:

* **`Customer`** — stores the user's name and login credentials and validates logins. The password is kept private (name-mangled) and only checked through a method.
* **`Account`** — the parent class holding everything shared by all accounts: the account number, balance, owner, transaction history, and the core methods (`deposit`, `withdrawal`, `transfer`, `get_balance`, `show_history`).
* **`SavingsAccount(Account)`** and **`CheckingAccount(Account)`** — child classes that inherit all of `Account`'s behavior and add their own: Savings adds an interest rate, Checking adds an overdraft limit.

This demonstrates two key OOP relationships:

* **Inheritance (IS-A):** a `SavingsAccount` *is a* type of `Account`, so it inherits deposits, withdrawals, and transfers rather than redefining them.
* **Composition (HAS-A):** an `Account` *has an* owner — it stores a `Customer` object rather than inheriting from it.

The accounts are created at startup, the user logs in once, and a menu loop routes each choice to the matching method on the correct account object.

## What I Learned

* Structuring a program with a parent class and child classes (inheritance)
* Using `super().__init__()` to reuse a parent's setup while adding child-specific attributes
* Composition — storing one object (a `Customer`) as an attribute of another (an `Account`)
* Encapsulation with private attributes and getter methods
* Deciding where data belongs — stored on the object (`__init__`) vs. passed into a method
* Building a menu loop and routing user input to the right object's methods

## Author

**Michael Murchie**

* GitHub: [MichaelTM0](https://github.com/MichaelTM0)
* LinkedIn: [michael-murchie](https://www.linkedin.com/in/michael-murchie/)
