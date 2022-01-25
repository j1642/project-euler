# Problem 7 - 10001st prime - did this in another notebook somewhere too
# https://projecteuler.net/problem=7
@time_this
def find_nth_prime(max_count: int):
    prime_count = 0
    test_num = 2
    while prime_count < max_count:
        for i in range(2, int(test_num ** 0.5) + 1):
            if test_num % i == 0:
                test_num += 1
                break
        else:
            prime_count += 1
            if prime_count == max_count:
                return test_num
            test_num += 1

find_nth_prime(10001)
