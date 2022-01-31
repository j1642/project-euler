# Problem 10 - Summation of primes
# https://projecteuler.net/problem=10
@time_this
def find_primes(max_num):
    primes = []
    for test_num in range(2, max_num):
        for i in range(2, int(test_num ** 0.5) + 1):
            if test_num % i == 0:
                break
        else:
            primes.append(test_num)
    return sum(primes)
            
find_primes(2000000)
