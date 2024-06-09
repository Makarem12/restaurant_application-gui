import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()

# Creating label and placing it using grid
header = ttk.Label(root, text="Restaurant Application", padding=(30, 10), font=("Arial", 20))
header.grid(column=0, row=0, columnspan=2, pady=(10, 20))

# Pizza section
pizza_label = ttk.Label(root, text="Pizza:", padding=(30, 10), font=("Arial", 17))
pizza_label.grid(column=0, row=1, sticky="E")

pizza_quantity_label = ttk.Label(root, text="Add pizza quantity:", padding=(30, 10), font=("Arial", 15))
pizza_quantity_label.grid(column=0, row=2, sticky="E")

pizza_quantity = ttk.Entry(root, width=5, font=("Arial", 15))
pizza_quantity.grid(column=1, row=2, sticky="W", padx=5, pady=5)
pizza_quantity.focus()

pizza_size_label = ttk.Label(root, text="Select pizza size:", padding=(30, 10), font=("Arial", 15))
pizza_size_label.grid(column=0, row=3, sticky="E")

pizza_size = ttk.Combobox(root, width=17, font=("Arial", 15))
pizza_size['values'] = ('Small', 'Medium', 'Large')
pizza_size.grid(column=1, row=3, sticky="W", padx=5, pady=5)
pizza_size.current(0)

# Burger section
burger_label = ttk.Label(root, text="Burger:", padding=(30, 10), font=("Arial", 17))
burger_label.grid(column=0, row=4, sticky="E")

burger_quantity_label = ttk.Label(root, text="Add burger quantity:", padding=(30, 10), font=("Arial", 15))
burger_quantity_label.grid(column=0, row=5, sticky="E")

burger_quantity = ttk.Entry(root, width=5, font=("Arial", 15))
burger_quantity.grid(column=1, row=5, sticky="W", padx=5, pady=5)
burger_quantity.focus()

burger_size_label = ttk.Label(root, text="Select burger size:", padding=(30, 10), font=("Arial", 15))
burger_size_label.grid(column=0, row=6, sticky="E")

burger_size = ttk.Combobox(root, width=17, font=("Arial", 15))
burger_size['values'] = ('Classic', 'Big')
burger_size.grid(column=1, row=6, sticky="W", padx=5, pady=5)
burger_size.current(0)

# Soft drinks section
soft_drinks_label = ttk.Label(root, text="Add Soft drinks quantity:", padding=(30, 10), font=("Arial", 15))
soft_drinks_label.grid(column=0, row=7, sticky="E")

soft_drinks_quantity = ttk.Entry(root, width=5, font=("Arial", 15))
soft_drinks_quantity.grid(column=1, row=7, sticky="W", padx=5, pady=5)
soft_drinks_quantity.focus()

# Order type section
order_type_label = ttk.Label(root, text="Select order type:", padding=(30, 10), font=("Arial", 15))
order_type_label.grid(column=0, row=8, sticky="E")

# Adding radio buttons for order type
order_type_var = tk.StringVar(value="Takeaway")
order_types = ["Takeaway", "Dine-In"]
for i, order_type in enumerate(order_types):
    radio_button = ttk.Radiobutton(root, text=order_type, value=order_type, variable=order_type_var)
    radio_button.grid(column=1, row=8+i, sticky="W", padx=5, pady=5)

# Adding checkboxes for extra options
extra_cheese_var = tk.IntVar()
extra_ketchup_var = tk.IntVar()

extra_cheese_checkbox = ttk.Checkbutton(root, text="Extra Cheese", variable=extra_cheese_var)
extra_cheese_checkbox.grid(column=0, row=10, sticky="W", padx=5, pady=5)

extra_ketchup_checkbox = ttk.Checkbutton(root, text="Extra Ketchup", variable=extra_ketchup_var)
extra_ketchup_checkbox.grid(column=1, row=10, sticky="W", padx=5, pady=5)

# Function to create the order summary, calculate the total price, and display it in a message box
def order_summary():
    pizza_quantity_val = pizza_quantity.get()
    pizza_size_val = pizza_size.get()
    burger_quantity_val = burger_quantity.get()
    burger_size_val = burger_size.get()
    soft_drinks_quantity_val = soft_drinks_quantity.get()
    order_type_val = order_type_var.get()
    extra_cheese_val = extra_cheese_var.get()
    extra_ketchup_val = extra_ketchup_var.get()
    
    if pizza_quantity_val and pizza_size_val and burger_quantity_val and burger_size_val and soft_drinks_quantity_val:
        # Calculate total price
        total_price = 0
        
        # Prices
        pizza_prices = {"Small": 5, "Medium": 7, "Large": 10}
        burger_prices = {"Classic": 5, "Big": 7}
        soft_drink_price = 2
        extra_price = 1
        
        total_price += int(pizza_quantity_val) * pizza_prices[pizza_size_val]
        total_price += int(burger_quantity_val) * burger_prices[burger_size_val]
        total_price += int(soft_drinks_quantity_val) * soft_drink_price
        if extra_cheese_val:
            total_price += extra_price
        if extra_ketchup_val:
            total_price += extra_price
        
        summary = (
            f"Pizza quantity: {pizza_quantity_val}\n"
            f"Pizza size: {pizza_size_val}\n"
            f"Burger quantity: {burger_quantity_val}\n"
            f"Burger size: {burger_size_val}\n"
            f"Soft drinks quantity: {soft_drinks_quantity_val}\n"
            f"Order type: {order_type_val}\n"
            f"Extra Cheese: {'Yes' if extra_cheese_val else 'No'}\n"
            f"Extra Ketchup: {'Yes' if extra_ketchup_val else 'No'}\n"
            f"Total Price: ${total_price}"
        )
        
        messagebox.showinfo("Order Summary", summary)

        # Clear the content of entry widgets
        pizza_quantity.delete(0, "end")
        burger_quantity.delete(0, "end")
        soft_drinks_quantity.delete(0, "end")
        
    else:
        messagebox.showwarning("Incomplete Information", "Please enter all required fields")

# Creating the Order Summary button with a purple color
order_summary_button = ttk.Button(root, text="Order Summary", cursor="hand2", command=order_summary)
order_summary_button.grid(column=0, row=11, columnspan=2, pady=10)

# Configure button color
style = ttk.Style()
style.configure("TButton", foreground="black", background="purple")
order_summary_button.configure(style="TButton")

root.mainloop()
