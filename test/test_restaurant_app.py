# test code is not mentioned in the assignment but I wrote it just in case
import pytest
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from restaurant_app.restaurant_app import order_summary  

def test_order_summary(monkeypatch):
    # Create a test root
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Create widgets for testing
    pizza_quantity = ttk.Entry(root)
    pizza_size = ttk.Combobox(root)
    burger_quantity = ttk.Entry(root)
    burger_size = ttk.Combobox(root)
    soft_drinks_quantity = ttk.Entry(root)
    order_type_var = tk.StringVar(value="Takeaway")
    extra_cheese_var = tk.IntVar()
    extra_ketchup_var = tk.IntVar()

    # Set test values
    pizza_quantity.insert(0, "2")
    pizza_size.set("Medium")
    burger_quantity.insert(0, "1")
    burger_size.set("Big")
    soft_drinks_quantity.insert(0, "3")
    extra_cheese_var.set(1)
    extra_ketchup_var.set(0)
    
    # Mock messagebox.showinfo
    def mock_showinfo(title, message):
        assert title == "Order Summary"
        assert "Pizza quantity: 2" in message
        assert "Pizza size: Medium" in message
        assert "Burger quantity: 1" in message
        assert "Burger size: Big" in message
        assert "Soft drinks quantity: 3" in message
        assert "Extra Cheese: Yes" in message
        assert "Extra Ketchup: No" in message
        assert "Total Price: $28" in message

    monkeypatch.setattr(messagebox, 'showinfo', mock_showinfo)
    
    # Test the order_summary function
    order_summary()

    # Clean up
    root.destroy()

if __name__ == "__main__":
    pytest.main()
