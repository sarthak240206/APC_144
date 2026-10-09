# Store visitor IDs from two different days in separate sets. Determine unique visitors across both days, returning visitors, visitors who came only on the first day, and visitors who came only on the second day.
# Program: Visitor IDs

day1 = {101, 102, 103, 104}
day2 = {103, 104, 105, 106}
print("Unique:", day1 | day2)
print("Returning:", day1 & day2)
print("Only day1:", day1 - day2)
print("Only day2:", day2 - day1)
