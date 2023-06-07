def find_max(lst):
    max_num = lst[0]
    max_index = 0

    for i in range(1, len(lst)):
        if lst[i] > max_num:
            max_num = lst[i]
            max_index = i

    return max_num, max_index

# Main program
if __name__ == '__main__':
    Lst = [1, 15, 2, 38, 48, 7, 16, 44]

    max_num, max_index = find_max(Lst)

    print("Max is", max_num, "at index", max_index)
