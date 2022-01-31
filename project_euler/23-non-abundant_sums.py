# Problem 23 - Non-abundant sums
# https://projecteuler.net/problem=23

# Find all abundant nums < 28123,
# Then, find all sums of every possibl pair of two abundant nums,
# Then, find nums which are not these (find deficient nums),
# Finally, find sum of these deficient nums

def sum_proper_divisors(num: int):
    low_divs = []
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            low_divs.append(i)
    high_divs = []
    for i in low_divs:
        high_divs.append(int(num / i))
    high_divs.remove(num)
    return sum(set(low_divs + high_divs))

@time_this
def abundants(max_range: int):
    abundants = []
    for num in range(1, max_range):
        if num < sum_proper_divisors(num):
            abundants.append(num)
    return abundants

@time_this
def abundant_pair_sums(abundants: list):
    pair_sums = []
    for i in abundants:
        for j in abundants:
            pair_sums.append(i + j)
    return set(pair_sums)

@time_this
def sum_deficient_nums(max_range: int, sums_abundant_pairs):
    deficient_nums = []
    for num in range(1, max_range):
        if num not in sums_abundant_pairs:
            deficient_nums.append(num)
            
    return sum(set(deficient_nums))

max_range = 28124
abundant_pair_sums = abundant_pair_sums(abundants(max_range))
sum_deficient_nums(max_range, abundant_pair_sums)
