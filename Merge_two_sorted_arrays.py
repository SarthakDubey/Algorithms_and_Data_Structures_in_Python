from heapq import merge


def merge_two(array1, array2):
    array = list(merge(array1, array2))
    return array


def main():
    array1 = [1, 3, 5, 7, 9]
    print(array1)
    array2 = [0, 2, 4, 6, 8, 10]
    print(array2)
    print(merge_two(array1, array2))


if __name__ == '__main__':
    main()
