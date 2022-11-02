def insertion_sort_ascending(input_array):
    for pos in range(1, len(input_array)):
        key = input_array[pos]
        last = pos - 1

        while last >= 0 and key < input_array[last]:
            input_array[last + 1] = input_array[last]
            last = last - 1

        input_array[last + 1] = key


def insertion_sort_descending(input_array):
    for pos in range(1, len(input_array)):
        key = input_array[pos]
        last = pos - 1

        while last >= 0 and key > input_array[last]:
            input_array[last + 1] = input_array[last]
            last = last - 1

        input_array[last + 1] = key


array = [9, 100, 54, 93, 10, 109]
insertion_sort_ascending(array)
print(array)
array = [9, 100, 54, 93, 10, 109]
insertion_sort_descending(array)
print(array)