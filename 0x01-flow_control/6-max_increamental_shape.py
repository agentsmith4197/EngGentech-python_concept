def print_shape(n):
    for i in range(1, n + 1):
        print("#" * i)

def get_user_input():
    while True:
        try:
            n = int(input("Enter an integer: "))
            return n
        except ValueError:
            print("Only integer characters are allowed. Try again.")

# Main program
if __name__ == '__main__':
    n = get_user_input()
    print_shape(n) 
