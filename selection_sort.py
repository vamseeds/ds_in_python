def selection_sort_ascending(input_array):
    for pos in range(len(input_array)):
        min_element_pos = pos
        for index in range(pos + 1, len(input_array)):
            if input_array[index] < input_array[min_element_pos]:
                min_element_pos = index
        if pos != min_element_pos:
            input_array[pos], input_array[min_element_pos] = input_array[min_element_pos], input_array[pos]


array = [9, 100, 54, 93, 10, 109]
selection_sort_ascending(array)
print(array)
