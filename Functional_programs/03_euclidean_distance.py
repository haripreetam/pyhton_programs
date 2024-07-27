import math

def euclidean_distance(x, y):
    return math.sqrt(x**2 + y**2)

x = int(input("enter x coordinate: "))
y = int(input("enter y coordinate: "))
distance = euclidean_distance(x, y)
print(f"the Euclidean distance from ({x}, {y}) to the origin (0, 0) is {distance}")
