# Your code here
import math
import random


# def slowfun_too_slow(x, y):
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653

#     return v


rand_nums = {}

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    xy_tuple = (x, y)

    if xy_tuple not in rand_nums:
        number = x ** y
        number = math.factorial(number)
        number //= (x + y)
        number %= 982451653

        rand_nums[xy_tuple] = number
        return rand_nums[xy_tuple]
    else:
        return rand_nums[xy_tuple]
        
# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
