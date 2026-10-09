# Represent the friends of two users using sets. Find mutual friends, friends unique to User 1, friends unique to User 2, and total unique friends.
# Program: Friends

user1 = {"Amit", "Priya", "Rahul", "Sneha"}
user2 = {"Priya", "Kiran", "Rahul", "Vijay"}
print("Mutual:", user1 & user2)
print("Unique to User1:", user1 - user2)
print("Unique to User2:", user2 - user1)
print("Total unique:", user1 | user2)
