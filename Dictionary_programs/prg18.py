dict1 = {
    "a": 10,
    "b": 20,
    "c": 30,
    "d": 40
}

dict2 = {
    "x": 20,
    "y": 30,
    "z": 50,
    "w": 60
}

common_values = set(dict1.values()) & set(dict2.values())

print("Common values:", common_values)
