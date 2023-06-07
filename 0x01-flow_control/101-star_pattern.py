def print_pattern(n):
    for i in range(1, n+1):
        print("* " * i)
    for i in range(n-1, 0, -1):
        print("* " * i)


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    print_pattern(num)
