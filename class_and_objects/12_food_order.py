class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self, tax_percent=5):
        subtotal = self.quantity * self.price
        return subtotal + subtotal * tax_percent / 100

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Total including tax: ₹", round(self.total_bill(), 2))

    def __del__(self):
        print("Order completed.")


order = FoodOrder(501, "Rahul", "Pizza", 2, 250)
order.display()
