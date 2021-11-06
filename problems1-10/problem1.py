'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''

import numpy as np

def find_sum_of_multiples(max_number):
    multiples = np.arange(3,max_number,3)
    multiples = np.append(multiples, np.arange(5,max_number,5))
    multiples_unique = np.unique(multiples)
    sum = np.sum(multiples_unique)
    return sum

result = find_sum_of_multiples(1000)

print(result)


