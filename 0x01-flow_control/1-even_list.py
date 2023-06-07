def list_add():
    numbers = [2, 8, 4, 18, 5, 7, 12, 9]
    return numbers

def list_even_sorted():
    numbers = list_add()
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_numbers.sort()
    return even_numbers

if __name__ == '__main__':
    even_sorted_list = list_even_sorted()
    print("Even & Sorted:", even_sorted_list)
 
