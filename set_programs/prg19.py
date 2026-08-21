morning = {"sarthak", "manjunath", "Priya", "Sneha"}
afternoon = {"namita", "balaji", "sarthak", "Sneha"}

print("Students present in both sessions:", morning & afternoon)
print("Students only in morning:", morning - afternoon)
print("Students only in afternoon:", afternoon - morning)
print("Students present in at least one session:", morning | afternoon)