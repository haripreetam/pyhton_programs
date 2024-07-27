def power_of_2():
    n = int(input("Enter the power value N"))
    while n < 0 or n >= 31:
        print("Value must be between 0 and 30.")
        n = int(input("Enter the power value N"))
    
    for i in range(n + 1):
        print(f"2^{i} = {2 ** i}")

power_of_2()
