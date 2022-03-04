import math

n = int(input("Input number of sides:"))
l = int(input("Input the length of a side: "))

print("The area of the polygon is: ", ((n * l ** 2) / (4 * math.tanh(180 / n))))