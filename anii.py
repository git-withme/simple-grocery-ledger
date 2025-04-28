
---

### 🛒 `product_ledger.py` full code:

```python
# Simple Ledger for a Single Product

class Product:
    def __init__(self, name, price_per_unit, quantity_in_stock):
        self.name = name
        self.price_per_unit = price_per_unit
        self.quantity_in_stock = quantity_in_stock
        self.quantity_sold = 0

    def sell(self, quantity):
        if quantity > self.quantity_in_stock:
            print(f"Only {self.quantity_in_stock} {self.name}(s) left in stock!")
        else:
            self.quantity_in_stock -= quantity
            self.quantity_sold += quantity
            print(f"Sold {quantity} {self.name}(s).")

    def show_ledger(self):
        total_sales = self.quantity_sold * self.price_per_unit
        print("\n--- Product Ledger ---")
        print(f"Product Name   : {self.name}")
        print(f"Price per Unit : ₹{self.price_per_unit}")
        print(f"Quantity Sold  : {self.quantity_sold}")
        print(f"Stock Left     : {self.quantity_in_stock}")
        print(f"Total Sales    : ₹{total_sales}")

# --- Main Program ---

# Create a product
apple = Product(name="Apple", price_per_unit=50, quantity_in_stock=100)

# Sell some units
apple.sell(20)
apple.sell(10)

# Display ledger
apple.show_ledger()
