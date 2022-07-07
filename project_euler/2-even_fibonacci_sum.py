# Problem 2 - Even Fibonacci numbers
# https://projecteuler.net/problem=2
def even_fib():
    '''Find sum of even Fibonacci numbers less than or equal to 4 million.'''
    a, b = 0, 1
    even_fibs = []
    while b <= 4000000:
        if b % 2 == 0:
            even_fibs.append(b)
        a, b = b, b + a

    return sum(even_fibs)

print(even_fib())
