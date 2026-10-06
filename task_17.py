```python
amount = 5000
records = []

def view_balance():
    print("Available Balance:", amount)

def add_money():
    global amount
    money = float(input("Enter amount to deposit: "))

    if money > 0:
        amount += money
        records.append("Deposit: " + str(money))
        print("Money added successfully")
    else:
        print("Enter a valid amount")

def take_money():
    global amount
    money = float(input("Enter amount to withdraw: "))

    if money <= 0:
        print("Invalid amount")
    elif money > amount:
        print("Not enough balance")
    else:
        amount -= money
        records.append("Withdrawal: " + str(money))
        print("Withdrawal completed")

def transactions():
    if len(records) == 0:
        print("No transactions found")
    else:
        print("Transaction Details:")
        for item in records:
            print(item)


while True:
    print("\n1. Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. History")
    print("5. Exit")

    option = input("Choose option: ")

    if option == "1":
        view_balance()
    elif option == "2":
        add_money()
    elif option == "3":
        take_money()
    elif option == "4":
        transactions()
    elif option == "5":
        print("Session ended")
        break
    else:
        print("Wrong option")
```
