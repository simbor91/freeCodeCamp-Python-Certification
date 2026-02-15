# Algorithms
# 022 Workshop: Build a Binary Search Algorithm

def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1

    # Binary search works by repeatedly narrowing down the search space
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)
        if value == value_at_middle:
            return path_to_target, f'Value found at index {mid}'
        elif value > value_at_middle:
            low = mid + 1 # if the value is greater than value_at_middle, it means the value must be in the right half of search area
        else:
            high = mid - 1 # if not in middle and not in the right area
    return [], 'Value not found'

print(binary_search([1, 2, 3, 4, 5], 3))
print(binary_search([1, 2, 3, 4, 5, 9], 4))
print(binary_search([1, 3, 5, 9, 14, 22], 10))