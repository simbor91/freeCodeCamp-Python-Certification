# 02 Loops and Sequences
# Lab: Build a Number Pattern Generator

def number_pattern(n):
    pattern = ''
    if not isinstance(n, int):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'
    for num in range(1,n+1):
        pattern += str(num)
        if num < n:
            pattern += ' '
    return pattern

print(number_pattern(12))