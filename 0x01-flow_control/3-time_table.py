def tt(number):
    print("Enter value:")
    print()
    print(f"{number} time_table")
    for i in range(1, 13):
        result = number * i
        print(f"{number} x {i} = {result}")
tt(2)