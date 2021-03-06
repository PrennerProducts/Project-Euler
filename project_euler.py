"""Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum 
of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000"""

def sum_of_multiples(x,y):
    sum = 0
    l=[]
    for i in range(3,1000):
        if i % 3 == 0:
            sum += i
            continue
        if i % 5 == 0:
            sum += i
            continue
    print(sum)
    



#sum_of_multiples(3,5)

"""Problem 2
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 
1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum 
of the even-valued terms."""


def fib_even():
    a, b = 0, 1
    even = 0
    while b < 4000000:
        a, b = b, a + b
        if b % 2 == 0:
            even+= b
        
                
    print(even)

#fib_even()

"""Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""

def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num%n==0:
            return False
    return True

def prime_factor(x):
    for i in range(2, x):
        if isprime(i) and x % i == 0:
            print(i)

#prime_factor(600851475143)



"""Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the
 product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def palindrome():
    l = []
    e = ""
    for i in range(10,99):
        for j in range(10,99):
            e = i * j
            e = str(e)
            
            if str(e) == str(e[::-1]):
                print(e)
            continue

palindrome()