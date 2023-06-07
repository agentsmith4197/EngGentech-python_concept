def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def divide(x, y):
    result = x / y
    return result

def multiply(x, y):
    result = x * y
    return result

def mod(x, y):
    result = x % y
    return result
if __name__ == '__main__':
    x = 2
    y = 3
    print("The addition of", x, "and", y, "=", add(x, y))

    x = 6
    y = 2
    print("The multiplication of", x, "and", y, "=", multiply(x, y)) 
