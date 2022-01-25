# Problem 6 - Sum square difference
# https://projecteuler.net/problem=6
@time_this
def sums_squares_diff(start: int, end: int):
    sum_of_squares = 0
    for i in range(start, end):
        # i * i seems 3x faster than i ** 2
        sum_of_squares += i * i
    
    square_of_sums = sum(range(start, end)) ** 2
    
    return square_of_sums - sum_of_squares
    
sums_squares_diff(1, 101)
