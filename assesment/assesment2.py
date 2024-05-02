import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database connection
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="product_management"
        )
        self.cursor = self.conn.cursor()

    def close(self):
        self.conn.close()

    def execute_query(self, query):
        self.cursor.execute(query)
        self.conn.commit()

    def fetch_data(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()


# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


# Product Manager class
class ProductManager(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def manage_stock(self):
        pass

    def view_stock(self):
        pass


# Customer class
class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def purchase_stock(self):
        pass

    def view_orders(self):
        pass


# GUI class
class ProductManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Product Management System")
        self.root.geometry("400x300")

        self.db = Database()

        # Login frame
        self.login_frame = tk.Frame(self.root)
        self.username_label = tk.Label(self.login_frame, text="Username:")
        self.username_entry = tk.Entry(self.login_frame)
        self.password_label = tk.Label(self.login_frame, text="Password:")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.register_button = tk.Button(self.login_frame, text="Register", command=self.register)

        # Product manager frame
        self.manager_frame = tk.Frame(self.root)
        self.manage_stock_button = tk.Button(self.manager_frame, text="Manage Stock", command=self.manage_stock)
        self.view_stock_button = tk.Button(self.manager_frame, text="View Stock", command=self.view_stock)

        # Customer frame
        self.customer_frame = tk.Frame(self.root)
        self.purchase_stock_button = tk.Button(self.customer_frame, text="Purchase Stock", command=self.purchase_stock)
        self.view_orders_button = tk.Button(self.customer_frame, text="View Orders", command=self.view_orders)

        # Current frame
        self.current_frame = None
        self.show_login()

    def show_login(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = self.login_frame
        self.current_frame.pack()
        self.username_label.pack()
        self.username_entry.pack()
        self.password_label.pack()
        self.password_entry.pack()
        self.login_button.pack()
        self.register_button.pack()

    def login(self):
        # Implement login logic here
        pass

    def register(self):
        # Implement registration logic here
        pass

    def manage_stock(self):
        # Implement stock management logic here
        pass

    def view_stock(self):
        # Implement stock viewing logic here
        pass

    def purchase_stock(self):
        # Implement purchase logic here
        pass

    def view_orders(self):
        # Implement orders viewing logic here
        pass

    def close(self):
        self.db.close()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ProductManagementApp(root)
    root.mainloop()
