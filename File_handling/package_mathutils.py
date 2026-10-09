from mathutils.basic import add, multiply
from mathutils.number import is_prime, is_armstrong
from mathutils.statistics import mean, maximum, minimum

print("Addition 15 + 25:", add(15, 25))
print("Multiplication 6 * 7:", multiply(6, 7))
print("Is 17 prime?:", is_prime(17))
print("Is 153 Armstrong?:", is_armstrong(153))

data = [12, 45, 67, 89, 23, 90]
print("Data:", data)
print("Mean:", mean(data))
print("Maximum:", maximum(data))
print("Minimum:", minimum(data))
