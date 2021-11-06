'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def find_square_diff(max_num):
    num_list = list(range(1,max_num+1))
    num_squared_list = [i**2 for i in num_list]
    sum_of_squares = sum(num_squared_list)
    square_of_sums = (sum(num_list))**2
    square_diff = square_of_sums - sum_of_squares
    return square_diff

result = find_square_diff(100)
print(result)