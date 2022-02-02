# Problem 25 - First 1000 digit Fibonacci number
# https://projecteuler.net/problem=25
@time_this
def fib_1000_digit():
    a, b = 1, 1
    # Initialize count as 2 because first two terms are the initial a, b vals
    count = 2
    
    while len(str(b)) < 1000:
        a, b = b, a + b
        count += 1
        
    return count

fib_1000_digit()
