'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

import math

def find_smallest_multiple(number):
    test_num = number 
    smallest_multiple = 0
    while(True):
        for i in range(number,1,-1):
            if test_num % i != 0:
                break
            if i == 2:
                smallest_multiple = test_num
        if smallest_multiple > 0:
            break
        test_num = test_num + 1
    return smallest_multiple

result = find_smallest_multiple(20)

print(result)