def quick_sort_helper(array, left, right):
    if left >= right:
        return

    pivot = left
    left = left + 1

    while right >= left:
        if array[left] > array[pivot] > array[right]:
            array[left], array[right] = array[right], array[left]
        elif left <= array[pivot]:
            left = left + 1
        elif right >= array[pivot]:
            right = right - 1

    array[pivot], array[right] = array[right], array[pivot]
    quick_sort_helper(array, pivot + 1, right - 1)
    quick_sort_helper(array, right + 1, len(array) - 1)


def quick_sort_ascending(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array


input_array = [9, 100, 54, 93, 10, 109]
input_array = quick_sort_ascending(input_array)
print(input_array)
