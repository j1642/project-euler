# Problem 20 - Factorial digit sum
# https://projecteuler.net/problem=20
# math.factorial(x) also available
@time_this
def factorial_digit_sum(num: int):
    factorial = 1
    for i in range(num, 1, -1):
        factorial *= i
        
    # Use int to str or list of mod 10 to get digits
    sum_digits = 0
    factorial = str(factorial)
    for digit in factorial:
        sum_digits += int(digit)
    
    #while factorial > 0:
    #    digits.append(num % 10)
    #    factorial = factorial // 10
        
    return sum_digits

factorial_digit_sum(100)
