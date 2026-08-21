d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 4, "c": 5, "d": 3}
common = d1.values() & d2.values()
print(common)
