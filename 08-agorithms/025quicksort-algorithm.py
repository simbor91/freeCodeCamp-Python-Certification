# Algorithms
# 025 Lab: Implement the Quicksort Algorithm

def quick_sort(array: list):
    if len(array) <= 1:
        return array
    
    pivot = array[0]

    less_pivot = []
    equal_pivot = []
    greater_pivot = []

    for value in array:
        if value < pivot: less_pivot.append(value)
        elif value == pivot: equal_pivot.append(value)
        else: greater_pivot.append(value)

    print(f'\nelements less than the pivot: {less_pivot}')
    print(f'elements equal to pivot: {equal_pivot}')
    print(f'elements greater than the pivot: {greater_pivot}')

    return quick_sort(less_pivot) + equal_pivot + quick_sort(greater_pivot)

if __name__ == '__main__': # implies that the current script is the main program, and not a module
    # print(f'Unsorted array: {[20, 3, 14, 1, 5]}')
    # print(f'Sorted array: {quick_sort([20, 3, 14, 1, 5])}')
    # print(f'Unsorted array: {[83, 4, 24, 2]}')
    # print(f'Sorted array: {quick_sort([83, 4, 24, 2])}')
    # print(f'Unsorted array: {[4, 42, 16, 23, 15, 8]}')
    # print(f'Sorted array: {quick_sort([4, 42, 16, 23, 15, 8])}')
    print(f'Unsorted array: {[87, 11, 23, 18, 18, 23, 11, 56, 87, 56]}')
    print(f'Sorted array: {quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])}')