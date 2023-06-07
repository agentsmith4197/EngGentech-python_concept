import math

def get_numeric_input(repeat):
    while True:
        try:
            value = float(input(repeat))
            return value
        except ValueError:
            print("Invalid input. Please enter a numerical value.")


def quad_fnx(a, b, c):
    equation = b**2 - 4*a*c

    if equation > 0:
        X1 = (-b + math.sqrt(equation)) / (2*a)
        X2 = (-b - math.sqrt(equation)) / (2*a)
        print("X1 = {:.2f}".format(X1))
        print("X2 = {:.2f}".format(X2))
    elif equation == 0:
        root = -b / (2*a)
        print("Root = {:.2f}".format(root))
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-equation) / (2*a)
        print("X1 = {:.2f} + {:.2f}i".format(real_part, imaginary_part))
        print("X2 = {:.2f} - {:.2f}i".format(real_part, imaginary_part))

if __name__ == '__main__':
    
    a =  get_numeric_input("Enter the coefficient of a: ")
    b = get_numeric_input("Enter the coefficient of b: ")
    c = get_numeric_input("Enter the coefficient of c: ")
    quad_fnx(a, b, c)
