def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while (low <= high):
        mid = (low + high) // 2
        guess = list[mid]
        if (guess == item):
            return mid
        if (guess > item):
            high = mid - 1
        else:
            low = mid + 1

    return None

# Testing it
my_list = [1, 3, 5, 7, 9]


print("Should return 1 as index: ", binary_search(my_list, 3))
print("Should return 4 as index: ", binary_search(my_list, 9))
print("Should return None: ", binary_search(my_list, -1))