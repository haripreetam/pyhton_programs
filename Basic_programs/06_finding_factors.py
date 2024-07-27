def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

def print_prime_factors():
    n = int(input("Enter a number to find the prime factors of it"))
    while n <= 0:
        print("Number must be a positive integer.")
        n = int(input("Enter a number to find the prime factors of it"))
    
    factors = prime_factors(n)
    print(f"The prime factors of {n} are: {factors}")

print_prime_factors()
