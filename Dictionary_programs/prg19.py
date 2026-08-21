

d = {"a": 1, "b": 2, "c": 1, "d": 2}
unique = {}
for k, v in d.items():
    if v not in unique.values():
        unique[k] = v
print(unique)
