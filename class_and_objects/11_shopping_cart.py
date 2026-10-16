class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, name, price, quantity=1):
        if price < 0 or quantity <= 0:
            print("Enter a valid price and quantity.")
            return
        if name in self.products:
            self.products[name]["quantity"] += quantity
        else:
            self.products[name] = {"price": price, "quantity": quantity}
        print(name, "added to cart.")

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]
            print(name, "removed from cart.")
        else:
            print("Product not found.")

    def total_bill(self):
        return sum(item["price"] * item["quantity"] for item in self.products.values())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Asha", "C101")
cart.add_product("Notebook", 50, 2)
cart.add_product("Pen", 10, 3)
print("Customer:", cart.customer_name)
print("Cart ID:", cart.cart_id)
print("Total bill: ₹", cart.total_bill())
cart.remove_product("Pen")
print("Updated bill: ₹", cart.total_bill())
