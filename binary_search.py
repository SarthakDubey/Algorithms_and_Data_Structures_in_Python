def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        middle = int((low + high) / 2)
        guess = list[middle]
        if guess == item:
            print("Item " + str(guess) + " found")
            return middle
        elif guess < item:
            low = middle + 1
        else:
            high = middle - 1
    return None


my_list = [x**2 for x in range(100)]
print("Position = " + str(binary_search(my_list, 81)))
