def iteration_binary_search(array, key):
    start = 0
    end = len(array)
    steps = 0
    while True:
        steps = steps + 1
        middle = int((start + end) / 2)
        if array[middle] == key:
            print(f'steps : {steps}')
            return middle
        elif array[middle] > key:
            end = middle
        else:
            start = middle
        if start == end:
            print(f'steps : {steps}')
            return -1


def recursion_helper(array, key, right, left):
    if right > left:
        return -1

    middle = (right + left) // 2
    middle_element = array[middle]
    if key == middle_element:
        return middle
    elif key > middle_element:
        return recursion_helper(array, key, middle + 1, left)
    else:
        return recursion_helper(array, key, right, middle - 1)


def recursion_binary_search(array, key):
    right = 0
    left = len(array)
    result = recursion_helper(array, key, right, left - 1)
    return result


iteration_result = iteration_binary_search([1, 2, 3, 4, 5, 8, 10, 99, 101, 108, 1022, 1995], 1)
recursion_result = recursion_binary_search([1, 2, 3, 4, 5, 8, 10, 99, 101, 108, 1022, 1995], 1)
print(f'iteration_result : {iteration_result}')
print(f'recursion_result : {recursion_result}')
