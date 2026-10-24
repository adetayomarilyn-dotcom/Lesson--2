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
            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menuquantities[item] = quantity_entry
        self.currency_var = tk.StringVar()
        ttk.Label(frame, text="Select Currency:", font=("Arial", 12)).grid(row=len(self.menuitems)+1, column=0, padx=10, pady=5)
        currency_dropdown = ttk.Combobox(frame, textvariable=self.currency_var, state="readonly", values=["USD", "INR"], width=18)
        currency_dropdown.grid(row=len(self.menuitems)+1, column=1, padx=10, pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)
        btn = ttk.Button(frame, text="Place Order", command=self.place_order)
        btn.grid(row=len(self.menuitems)+2, columnspan=3, padx=10, pady=10)
    def setup_background(self, root):
        bg_width = 800
        bg_height = 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()
        image = tk.PhotoImage(file="background1.png")
        background_image = image.subsample(image.width() // bg_width, image.height() // bg_height)
        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exhangerate if currency == "INR" else 1
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exhangerate if currency == "INR" else 1
        for item, entry in self.menuquantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int (quantity)
                price = self.menuitems[item] * rate
                cost = price * quantity
                total_cost += cost
                if quantity > 0:
                    order_summary += f"{item} : {quantity} x {symbol}{price:.2f} = {symbol}{cost:.2f}\n"
        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost:.2f}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("No Items Selected", "Please select at least one item to place an order.")
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()


