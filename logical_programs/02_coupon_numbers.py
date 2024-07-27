import random

def generate_coupons(n):
    distinct_coupons = set()
    total_random_numbers = 0

    while len(distinct_coupons) < n:
        random_number = random.randint(0, n-1)
        total_random_numbers += 1
        distinct_coupons.add(random_number)

    print(f"total random numbers needed: {total_random_numbers}")

n = int(input("enter the number of distinct coupon numbers: "))
generate_coupons(n)
