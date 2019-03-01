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


l = [x**2 for x in range(100)]
my_list = l
print("Position = " + str(binary_search(my_list, 81)))


def binarySearch(list, item, low, high):
    if high >= low:
        middle = low + (high-low) // 2
        if list[middle] == item:
            return (list[middle], middle)
        elif list[middle] > item:
            return binarySearch(list, item, low, middle-1)
        else:
            return binarySearch(list, item, middle+1, high)
    else:
        return -1


print(binarySearch(l, 81, 0, len(l)-1))
