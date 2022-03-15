# Problem 44 - Pentagon Numbers
# https://projecteuler.net/problem=44

# From an earlier problem, searching large sorted lists is a speed bottleneck.
# Wikipedia page for pentagonal numbers has an equation to check if a number
#    is pentagonal, which is faster than searching the pentagonal_nums list.
# Also read that python sets are hash tables, so checking membership is generally
#    much faster for sets than checking membership in lists.

# Checks list of 7000 pentagonal numbers in 11.5 sec.

# TODO: How to define upper bound? Also, how to increase speed?

@time_this
def find_pentagonal_pairs(total_pentagonal_nums: int):
    '''Return the pair of pentagonal numbers for which their sum and difference
    are each also pentagonal, and the absolute value of the difference is 
    minimized.
    '''
    pentagonal_nums = []
    # First pentagonal number is 1, not 0. So n starts at 1.
    for n in range(1, total_pentagonal_nums):
        num = (n * (3 * n - 1)) // 2
        pentagonal_nums.append(num)
    
    for i in pentagonal_nums:
        i_index = pentagonal_nums.index(i)
        # Only use j values which are less than current i value
        for j in pentagonal_nums[:i_index]:
            # If result is an integer, i + j is a pentagonal number.
            pentag_test_add = ((24 * (i + j) + 1) ** 0.5 + 1) / 6
            
            if pentag_test_add == int(pentag_test_add):
                # If result is an integer, i - j is a pentagonal number.
                pentag_test_subtract = ((24 * (i - j) + 1) ** 0.5 + 1) / 6
                
                if abs(pentag_test_subtract) == abs(int(pentag_test_subtract)):
                    try:
                        if min_difference > abs(i - j):
                            min_difference = abs(i - j)
                    # Initialize min_difference variable with a relevant number,
                    #   instead of with an arbitrary high number guess.
                    except NameError:
                        min_difference = abs(i - j)
                        continue
                    
    return min_difference
        
find_pentagonal_pairs(5000)

