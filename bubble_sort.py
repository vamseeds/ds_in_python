def bubble_sort_ascending(input_array):
    for iteration in range(len(input_array)):
        for index in range(0, len(input_array) - 1 - iteration):
            if input_array[index] > input_array[index + 1]:
                input_array[index], input_array[index + 1] = input_array[index + 1], input_array[index]


def bubble_sort_descending(input_array):
    for iteration in range(len(input_array)):
        for index in range(0, len(input_array) - 1 - iteration):
            if input_array[index] < input_array[index + 1]:
                input_array[index], input_array[index + 1] = input_array[index + 1], input_array[index]


array = [9, 100, 54, 93, 10, 109]
bubble_sort_ascending(array)
print(array)
bubble_sort_descending(array)
print(array)
