# Algorithms
# Lab 026: Implement the Selection Sort Algorithm

# time complexity O(n^2)
# space complexity O(1)

def selection_sort(array):
    n = len(array)
    
    for i in range(n):
        min_index = i
        
        # Cerchiamo il minimo nella parte non ordinata
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        
        # OTTIMIZZAZIONE: Scambiamo solo se il minimo trovato non è già nella posizione corrente (i)
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            
    return array

if __name__ == '__main__': # implies that the current script is the main program, and not a module
    print('unsorted array: [33, 1, 89, 2, 67, 245]')
    print(f'sorted array: {selection_sort([33, 1, 89, 2, 67, 245])}')
    print('unsorted array: [5, 16, 99, 12, 567, 23, 15, 72, 3]')
    print(f'sorted array: {selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3])}')