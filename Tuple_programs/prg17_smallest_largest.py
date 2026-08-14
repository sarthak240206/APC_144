tup = (34,54,67,89,12,300,42,1)
print("The tuple is:", tup)
larget = tup[0]
smallest = tup[0]
for i in range(len(tup)):
    if tup[i] > larget:
        larget = tup[i]
    elif tup[i] < smallest:
        smallest = tup[i]
print("The largest element in the tuple is:", larget)
print("The smallest element in the tuple is:", smallest)
