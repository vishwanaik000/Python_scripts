import math

count = 0
def print_factors(x):
   
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)

           
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n



'''def isPrime(n):
    for i in range(2, n/2):
        if(num % i == 0):
            '''

num = int(input("Enter a number: "))

print_factors(num)


n = print_factors(num)

m = largest_prime_factor(num)

print m
    

    







    
