'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

import math 

def find_largest_prime(number):

    largest_prime = 0

    while number % 2 == 0:

        largest_prime = 2

        number = number / 2
    
    for i in range(3,int(math.sqrt(number)+1),2):
        while number % i == 0:
            largest_prime = i
            number = number / i

    if number > 2:
        largest_prime = number

    return largest_prime

result = find_largest_prime(600851475143)

print(result)

