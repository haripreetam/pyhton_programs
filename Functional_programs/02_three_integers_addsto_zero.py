def find_sums_of_zero(arr):
    n = len(arr)
    found = False
    triplets = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    triplets.append((arr[i], arr[j], arr[k]))
                    found = True
    if not found:
        print("no triplets found.")
    else:
        print(f"number of triplets: {len(triplets)}")
        for triplet in triplets:
            print(triplet)

n = int(input("enter the number of integers: "))
arr = list(map(int, input("enter the integers: ").split()))
find_sums_of_zero(arr)
