def create_2d_array():
    rows = int(input("enter the number of rows: "))
    cols = int(input("enter the number of columns: "))
    
    array = []
    print("enter the elements row-wise:")
    for i in range(rows):
        row = list(map(int, input().split()))
        while len(row) != cols:
            print(f"please enter exactly {cols} elements.")
            row = list(map(int, input().split()))
        array.append(row)
    
    print("2D Array:")
    for row in array:
        print(" ".join(map(str, row)))

create_2d_array()
