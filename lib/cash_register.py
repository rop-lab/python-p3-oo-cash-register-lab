class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount

    def add_item(self, item, price, quantity=1):
        self.items.extend([item] * quantity)  # Use extend to add multiple items
        self.total += price * quantity
        return f"Added {quantity} {item}(s) to the cart. Total: ${self.total}"

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
            return self.total
        else:
            print("There is no discount to apply.")
            return self.total

    def void_last_transaction(self):
        if self.items:
            last_item, last_price, last_quantity = self.items.pop()
            self.total -= last_price * last_quantity
            return self.total  # Return the updated total after voiding the last transaction
        else:
            return "There are no transactions to void."

    def get_item_price(self, item):
        for i in range(len(self.items) - 1, -1, -1):
            current_item, price, quantity = self.items[i]
            if current_item == item:
                return price
        return None

    def get_item_total(self, item):
        return sum(price * quantity for name, price, quantity in self.items if name == item)

    def get_item_quantity(self, item):
        return sum(quantity for name, price, quantity in self.items if name == item)

    def reset_register_totals(self):
        self.total = 0.0
        self.items = []

    def get_all_items(self):
        return [item for item in self.items]  # Extract item names from tuples

    def get_all_items_including_multiples(self):
        return [f"{item} ({self.items.count(item)})" for item in set(self.items)]  # Count occurrences for multiples
