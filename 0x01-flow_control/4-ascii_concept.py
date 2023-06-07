def check(char):
    while True:
        if len(char) != 1:
            print("Not more than one character at a time, try again")
            char = input("Enter a single character: ")
            continue

        if not char.isalpha():
            print("Non-alphabetical character is not allowed, please try again")
            char = input("Enter a single character: ")
            continue

        if ord('a') <= ord(char) <= ord('z'):
            print(f"The input {char} is a lower case character")
        elif ord('A') <= ord(char) <= ord('Z'):
            print(f"The input {char} is an upper case character")
        
        break 
check('a')