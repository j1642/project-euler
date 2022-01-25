# Problem 2 - Even Fibonacci numbers
# https://projecteuler.net/problem=2
def even_fib():
    a, b = 0, 1
    even_fibs = []
    while b <= 4000000:
        if b % 2 == 0:
            even_fibs.append(b)
        a, b = b, b + a
        
    return sum(even_fibs)
        
even_fib()
