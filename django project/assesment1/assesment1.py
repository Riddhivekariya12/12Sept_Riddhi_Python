class FruitManager:
    def __init__(self):
        self.fruit_stock = {}  # Dictionary to store fruit stock

    def add_fruit(self, fruit_name, quantity):
        """Add fruit to the stock"""
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] += quantity
        else:
            self.fruit_stock[fruit_name] = quantity

    def view_stock(self):
        """View current fruit stock"""
        print("Current Fruit Stock:")
        for fruit, quantity in self.fruit_stock.items():
            print(f"{fruit}: {quantity}")

    def update_stock(self, fruit_name, quantity):
        """Update existing fruit stock"""
        if fruit_name in self.fruit_stock:
            self.fruit_stock[fruit_name] = quantity
        else:
            print("Fruit not found in stock.")


# Example usage of the Fruit Manager module
if __name__ == "__main__":
    manager = FruitManager()

    while True:
        print("\nFruit Store Management System")
        print("1. Add Fruit")
        print("2. View Fruit Stock")
        print("3. Update Fruit Stock")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            fruit = input("Enter fruit name: ")
            quantity = int(input("Enter quantity: "))
            manager.add_fruit(fruit, quantity)
            print("Fruit added to stock.")

        elif choice == "2":
            manager.view_stock()

        elif choice == "3":
            fruit = input("Enter fruit name to update: ")
            quantity = int(input("Enter updated quantity: "))
            manager.update_stock(fruit, quantity)
            print("Stock updated.")

        elif choice == "4":
            print("Thank you for using the Fruit Store Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
