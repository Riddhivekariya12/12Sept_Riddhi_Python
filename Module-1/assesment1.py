class FruitManager:
    def _init_(self):
        self.fruit_stock = {}

    def add_fruit_stock(self, fruit_name, quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
        else:
            self.fruit_stock[fruit_name] = quantity

    def view_fruit_stock(self):
        print("\nFruit Stock:")
        for fruit, quantity in self.fruit_stock.items():
            print(f"{fruit}: {quantity} units")

    def update_fruit_stock(self, fruit_name, new_quantity):
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = new_quantity
            print(f"{fruit_name} quantity updated to {new_quantity}")
        else:
            print(f"{fruit_name} not found in stock")

# Customer.py
class Customer:
    def _init_(self):
        self.transactions = []

    def view_all_transactions(self):
        print("\nAll Transactions:")
        for transaction in self.transactions:
            print(transaction)

# Controller.py
from FruitManager import FruitManager
from Customer import Customer

def main():
    fruit_manager = FruitManager()
    customer = Customer()

    while True:
        print("\nMenu:")
        print("1. Add Fruit Stock")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        print("4. View All Transactions")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            fruit_name = input("Enter fruit name: ")
            quantity = int(input("Enter quantity: "))
            fruit_manager.add_fruit_stock(fruit_name, quantity)
            customer.transactions.append(f"Added {quantity} units of {fruit_name} to stock")

        elif choice == '2':
            fruit_manager.view_fruit_stock()

        elif choice == '3':
            fruit_name = input("Enter fruit name: ")
            new_quantity = int(input("Enter new quantity: "))
            fruit_manager.update_fruit_stock(fruit_name, new_quantity)
            customer.transactions.append(f"Updated {fruit_name} quantity to {new_quantity}")

        elif choice == '4':
            customer.view_all_transactions()

        elif choice == '5':
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if _name_ == "_main_":
    main()