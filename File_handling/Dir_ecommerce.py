import os
import sys

sys.path.insert(0, os.path.abspath("ecommerce"))

from products.catalog import get_product
from products.inventory import check_stock
from customers.profile import get_customer
from customers.auth import authenticate
from orders.cart import create_cart
from orders.checkout import process_checkout
from payments.gateway import process_payment
from payments.invoice import generate_invoice

if authenticate("user1", "pass123"):
    customer = get_customer("C001", "Rahul Kumar")
    product = get_product("P101", "Wireless Headphones", 2500)
    in_stock = check_stock("P101", 10)

    cart = create_cart([product])
    order = process_checkout(customer["id"], cart)
    payment = process_payment(order["order_id"], order["total"])
    invoice = generate_invoice(order["order_id"], customer["name"], order["total"])

    print("Customer:", customer["name"])
    print("Order ID:", order["order_id"])
    print("Payment Status:", payment["status"])
    print("Invoice Generated:", invoice)
