'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def find_nth_prime(n):

    prime_list = []
    x = 2
    prime_list.append(x)
    while len(prime_list)<n:
        x = x+1
        for i in range(len(prime_list)):
            if x % prime_list[i] == 0:
                break
            if i == len(prime_list) - 1:
                prime_list.append(x)
    return prime_list[-1]

result = find_nth_prime(10001)

print(result)
            

            