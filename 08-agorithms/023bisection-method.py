# Algorithms
# 023 Lab: Implement the Bisection Method

def square_root_bisection(value, tolerance=1e-8, max_iter=2):
    if value < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif value == 0:
        print('The square root of 0 is 0')
        return value
    elif value == 1:
        print('The square root of 1 is 1')
        return value
    elif value > 1:
        upper_limit = value
        lower_limit = 0
        count = 1
        while upper_limit - lower_limit > tolerance:
            mid = (upper_limit + lower_limit) / 2
            if mid*mid > value:
                upper_limit = mid
            else:
                lower_limit = mid
            count += 1
            if count >= max_iter:
                print(f'Failed to converge within {max_iter} iterations')
                return None
        print(f'The square root of {value} is approximately {mid}')
        return mid

    elif value < 1:
        upper_limit = 1
        lower_limit = value
        count = 1
        while upper_limit - lower_limit > tolerance:
            mid = (upper_limit + lower_limit) / 2
            if mid*mid > value:
                upper_limit = mid
            else:
                lower_limit = mid
            count += 1
            if count >= max_iter:
                print(f'Failed to converge within {max_iter} iterations')
                return None
        print(f'The square root of {value} is approximately {mid}')
        return mid

square_root_bisection(0)
square_root_bisection(1)
square_root_bisection(0.001, 1e-7, 50)
square_root_bisection(0.25, 1e-7, 50)
square_root_bisection(81, 1e-3, 50)
square_root_bisection(225, 1e-3, 100)
square_root_bisection(225, 1e-5, 100)
square_root_bisection(225, 1e-7, 100)
square_root_bisection(225, 1e-7, 10)