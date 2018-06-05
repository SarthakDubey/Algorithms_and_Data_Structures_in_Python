def merge(left_half, right_half):
    left_index, right_index, result = 0, 0, []
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index+=1
        else:
            result.append(right_half[right_index])
            right_index+=1
    result += left_half[left_index:]
    result += right_half[right_index:]
    return result

def merge_sort(array):
    if len(array) <= 1:
        return array
    length = len(array)//2
    left_half = merge_sort(array[:length])
    right_half = merge_sort(array[length:])

    return merge(left_half, right_half)

print(merge_sort([1,7,3,7,2,8,9,3,5,1,4,8,23,6,12,34,62,4456,234,56,72,3,2,6,43,346,567,42,8,423,635,68,234,357,457]))

import heapq
heapq.heapify([1, 7, 3, 7, 2, 8, 9, 3, 5, 1, 4, 8, 23, 6, 12, 34, 62, 4456, 234,
         56, 72, 3, 2, 6, 43, 346, 567, 42, 8, 423, 635, 68, 234, 357, 457])
