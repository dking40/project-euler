'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def find_largest_palindrome(number):
    largest_palindrome = 0
    num1 = num2 = number
    while num1 > 0 and num2 > 0:
        prod_list = list(str(num1*num2))
        if prod_list == prod_list[::-1]:
            prod = int("".join(prod_list))
            if prod > largest_palindrome:
                largest_palindrome = prod
        if num1 == 1 and num2 == 1:
            break
        elif num2>1:
            num2 = num2 - 1
        else:
            num1 = num1 - 1
            num2 = num1
    return largest_palindrome

result = find_largest_palindrome(999)

print(result)