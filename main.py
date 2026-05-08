#Banking system Simulation:

# In-memory database
bank_db = {}

# Function to create account
def create_account(acc_no, name, initial_balance=0):
    if acc_no in bank_db:
        print("Account already exists!")
        return
    
    bank_db[acc_no] = {
        "name": name,
        "balance": initial_balance
    }
    print(f"Account created successfully for {name}")

# Function to deposit money
def deposit(acc_no, amount):
    if acc_no not in bank_db:
        print("Account not found!")
        return
    
    if amount <= 0:
        print("Invalid deposit amount!")
        return
    
    bank_db[acc_no]["balance"] += amount
    print(f"Deposited ₹{amount}. New Balance: ₹{bank_db[acc_no]['balance']}")

# Function to withdraw money
def withdraw(acc_no, amount):
    if acc_no not in bank_db:
        print("Account not found!")
        return
    
    if amount <= 0:
        print("Invalid withdrawal amount!")
        return
    
    if bank_db[acc_no]["balance"] < amount:
        print("Insufficient balance!")
        return
    
    bank_db[acc_no]["balance"] -= amount
    print(f"Withdrawn ₹{amount}. Remaining Balance: ₹{bank_db[acc_no]['balance']}")

# Function to check balance
def check_balance(acc_no):
    if acc_no not in bank_db:
        print("Account not found!")
        return
    
    print(f"Account Holder: {bank_db[acc_no]['name']}")
    print(f"Balance: ₹{bank_db[acc_no]['balance']}")

# Function to display all accounts (admin purpose)
def display_all_accounts():
    for acc, details in bank_db.items():
        print(f"Acc No: {acc}, Name: {details['name']}, Balance: ₹{details['balance']}")

# Menu-driven system
def banking_system():
    while True:
        print("\n--- Banking System ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Display All Accounts")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            acc_no = input("Enter Account Number: ")
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))
            create_account(acc_no, name, balance)

        elif choice == '2':
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount: "))
            deposit(acc_no, amount)

        elif choice == '3':
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount: "))
            withdraw(acc_no, amount)

        elif choice == '4':
            acc_no = input("Enter Account Number: ")
            check_balance(acc_no)

        elif choice == '5':
            display_all_accounts()

        elif choice == '6':
            print("Exiting system...")
            break

        else:
            print("Invalid choice!")

# Main Function
if __name__ == "__main__":
    # Run the system
    banking_system()