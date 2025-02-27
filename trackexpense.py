import tkinter as tk
from tkinter import messagebox

expenses = []

def add_expense():
    item = item_entry.get()
    amount = amount_entry.get()
    if item and amount:
        try:
            expenses.append((item, float(amount)))
            item_entry.delete(0, tk.END)
            amount_entry.delete(0, tk.END)
            show_expenses()
        except ValueError:
            messagebox.showwarning("Input Error", "Enter a valid number for amount")
    else:
        messagebox.showwarning("Input Error", "Please enter both item and amount")

def show_expenses():
    listbox.delete(0, tk.END)
    for i, (item, amount) in enumerate(expenses, 1):
        listbox.insert(tk.END, f"{i}. {item}: ${amount}")

def delete_expense():
    try:
        selected_index = listbox.curselection()[0]
        expenses.pop(selected_index)
        show_expenses()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an expense to delete")

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Item:").grid(row=0, column=0)
item_entry = tk.Entry(root)
item_entry.grid(row=0, column=1)

tk.Label(root, text="Amount:").grid(row=1, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=1, column=1)

tk.Button(root, text="Add Expense", command=add_expense).grid(row=2, columnspan=2)
listbox = tk.Listbox(root, width=40)
listbox.grid(row=3, columnspan=2)

tk.Button(root, text="Delete Expense", command=delete_expense).grid(row=4, columnspan=2)

root.mainloop()
