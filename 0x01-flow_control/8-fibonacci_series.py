def fib(numb):
    fib_list = [0, 1]

    while fib_list[-1] <= numb:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)

    fib_list = fib_list[:-1] 

    fib_series = ", ".join(map(str, fib_list))
    print("Fib Series:", fib_series)


if __name__ == '__main__':
    num = int(input("Enter a number: "))
    fib(num)
