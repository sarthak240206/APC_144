day1_visitors = {101, 102, 103, 104, 105}
day2_visitors = {103, 104, 105, 106, 107}

unique_visitors = day1_visitors | day2_visitors
returning_visitors = day1_visitors & day2_visitors
only_first_day = day1_visitors - day2_visitors
only_second_day = day2_visitors - day1_visitors

print("Unique visitors:", unique_visitors)
print("Returning visitors:", returning_visitors)
print("Visitors only on first day:", only_first_day)
print("Visitors only on second day:", only_second_day)

# Products belonging to two categories
category1 = {"Laptop", "Mouse", "Keyboard", "Monitor"}
category2 = {"Mouse", "Printer", "Monitor", "Scanner"}

common_products = category1 & category2

print("Products in both categories:", common_products)