cities = {
    "Mumbai": 20400000,
    "Delhi": 32900000,
    "Pune": 7400000,
    "Bangalore": 13600000,
    "Chennai": 12000000
}

city_to_remove = "Pune"
cities.pop(city_to_remove)

print("Updated city dictionary:")
for city, population in cities.items():
    print(city, ":", population)
