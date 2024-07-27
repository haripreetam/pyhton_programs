import random

def flip_coin():
    num_flips = int(input("Enter the number of flips"))
    while num_flips <= 0:
        print("Number of flips must be a positive integer.")
        num_flips = int(input("Enter the number of flips"))
    
    heads = 0
    for _ in range(num_flips):
        if random.random() < 0.5:
            heads += 1
    
    tails = num_flips - heads
    print(f"Percentage of Heads: {heads / num_flips * 100}%")
    print(f"Percentage of Tails: {tails / num_flips * 100}%")

flip_coin()
