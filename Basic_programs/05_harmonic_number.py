def harmonic_num(n):
    harmonic_sum = 0.0
    for i in range(1, n + 1):
        harmonic_sum += 1 / i
    return harmonic_sum

def print_harmonic_number():
    n = int(input("Enter the harmonic value N"))
    while n == 0:
        print("N cannot be 0")
        n = int(input("Enter the harmonic value N"))
    
    harmonic_sum = harmonic_num(n)
    print(f"The {n}th Harmonic Value is: {harmonic_sum}")

print_harmonic_number()
