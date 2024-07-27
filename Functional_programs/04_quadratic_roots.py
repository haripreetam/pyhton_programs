import math

def find_roots(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        print("the equation has no real roots.")
    elif delta == 0:
        root = -b / (2*a)
        print(f"the equation has one root: {root}")
    else:
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"the roots of the equation are: {root1} and {root2}")

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
find_roots(a, b, c)
