import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management")
        self.menuitems = {
            "Fries": 2,
            "Burger meal deal": 5,
            "Fanta": 1,
            "Wrap meal plan": 7,
            "Pizza": 3

        }
        self.exhangerate = 82
        self.setup_background(root)
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor= tk.CENTER)
        ttk.Label(frame, text= "Restaurant Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menulabels={}
        self.menuquantities={}
        for i, (item, price) in enumerate(self.menuitems.items(), start=1):
            label = ttk.Label(frame, text=f"{item} (${price})", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menulabels[item]=label