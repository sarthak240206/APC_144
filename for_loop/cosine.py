import math

x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

cosx = 1
sign = -1

for i in range(2, 2 * n, 2):
    term = (x ** i) / math.factorial(i)
    cosx = cosx + sign * term
    sign = -sign

print("Cos(x) using series =", cosx)
print("Cos(x) using math.cos() =", math.cos(x))
