import tkinter as tk
from tkinter import messagebox
import mysql.connector

def register_user(user_type):
    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    gender = gender_var.get()
    city = city_entry.get()
    state = state_entry.get()

    # Insert data into MySQL database
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Product_Management',
                                             user='root',
                                             password='')
        cursor = connection.cursor()
        if user_type == 'ProductManager':
            table = 'Product_Managers'
        else:
            table = 'Customers'
        sql = f"INSERT INTO {table} (name, contact, email, gender, city, state) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, contact, email, gender, city, state)
        cursor.execute(sql, values)
        connection.commit()
        messagebox.showinfo("Success", "Registration successful!")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Create main window
root = tk.Tk()
root.title("Product Management Registration")

# Labels
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Contact:").grid(row=1, column=0)
tk.Label(root, text="Email:").grid(row=2, column=0)
tk.Label(root, text="Gender:").grid(row=3, column=0)
tk.Label(root, text="City:").grid(row=4, column=0)
tk.Label(root, text="State:").grid(row=5, column=0)

# Entries
name_entry = tk.Entry(root)
contact_entry = tk.Entry(root)
email_entry = tk.Entry(root)
city_entry = tk.Entry(root)
state_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
contact_entry.grid(row=1, column=1)
email_entry.grid(row=2, column=1)
city_entry.grid(row=4, column=1)
state_entry.grid(row=5, column=1)

# Gender Radiobuttons
gender_var = tk.StringVar()
gender_var.set("Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=3, column=1)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=3, column=2)

# Register buttons
tk.Button(root, text="Register as Product Manager", command=lambda: register_user('ProductManager')).grid(row=6, column=0, columnspan=2, pady=5)
tk.Button(root, text="Register as Customer", command=lambda: register_user('Customer')).grid(row=7, column=0, columnspan=2, pady=5)

root.mainloop()


