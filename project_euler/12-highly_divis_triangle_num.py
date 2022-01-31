# Problem 12 - Highly divisible triangular number
# https://projecteuler.net/problem=12
def find_divisors(number: int):
    'Return set of divisors of a number, including 1 and the number itself'
    low_divisors = []
    high_divisors = []
    
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            low_divisors.append(i)
    for divisor in low_divisors:
        high_divisors.append(int(number / divisor))
    num_divisors = len(set(low_divisors + high_divisors))
    return num_divisors

@time_this
def highly_divis_tri_num(max_range: int):
    divisible_by = {1: 1}
    triangle_nums = [1]
    for i in range(2, max_range):
        triangle_nums.append(triangle_nums.pop() + i)
        divisible_by[triangle_nums[0]] = find_divisors(triangle_nums[0])
    
    max_amount_divisors = 0
    for k, v in divisible_by.items():
        if v > max_amount_divisors:
            max_amount_divisors = v
            if v >= 500:
                print(k, v)
                break
    
    return max_amount_divisors


highly_divis_tri_num(19000)

