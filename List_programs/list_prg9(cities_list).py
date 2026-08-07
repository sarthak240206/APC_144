cities = ["kolhapur","pune","mumbai","nagpur","latur"]
city = input("Enter city")
city.lower()
for i in cities:
    if i == city:
        print("City exists in list of cities")
