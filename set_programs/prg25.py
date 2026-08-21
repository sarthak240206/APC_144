user1_friends = {"sarthak", "satyajeet", "manjunath", "parshwa"}
user2_friends = {"vaishnavi", "sarthak", "Vikram", "parswha"}

mutual_friends = user1_friends & user2_friends
unique_user1 = user1_friends - user2_friends
unique_user2 = user2_friends - user1_friends
total_unique_friends = user1_friends | user2_friends

print("Mutual friends:", mutual_friends)
print("Friends unique to User 1:", unique_user1)
print("Friends unique to User 2:", unique_user2)
print("Total unique friends:", total_unique_friends)