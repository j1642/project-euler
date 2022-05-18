# Problem 58 - Spiral Primes
# https://projecteuler.net/problem=58
# Related to Problem 28 and Ulam spiral

# Huge performance increase after removing redundant is_prime() calculations
# Fermat possible prime test is slower than is_prime()?
# is_prime() speed increased ~2x by only iterating odd nums for trial division

@time_this
def spiral_primes(max_layers: int):
    '''Return length of a side of a square spiral of consecutive integers
    (Ulam spiral) when the percentage of prime numbers along the diagonals
    first falls below 10%.
    '''
    # Layer 0 of the number spiral only contains number 1
    all_nums_on_diagonals = [1]
    bottom_right_diag = []
    prime_count = 0
    total_num_count = 1
    found_primes = []
    
    for test_max_layer in range(1, max_layers):
        layer_side_length = 2 * test_max_layer + 1

        bottom_right_diag.append((test_max_layer * 2 + 1) ** 2)

        top_right_num = bottom_right_diag[-1] - 6 * test_max_layer
        top_left_num = bottom_right_diag[-1] - 4 * test_max_layer
        bottom_left_num = bottom_right_diag[-1] - 2 * test_max_layer
        
        all_nums_on_diagonals.append(bottom_right_diag[-1])
        all_nums_on_diagonals.append(top_right_num)
        all_nums_on_diagonals.append(top_left_num)
        all_nums_on_diagonals.append(bottom_left_num)
        
        new_nums = [bottom_right_diag[-1],
                    top_right_num,
                    top_left_num,
                    bottom_left_num]
        
        # Update total_num_count and primes with the four new diag numbers
        for num in new_nums:
            total_num_count += 1
            if is_prime(num):
                found_primes.append(num)
                prime_count += 1

        approx_percent_prime = prime_count / total_num_count * 100
        if approx_percent_prime < 10:
            
            return layer_side_length
        
def is_prime(num: int) -> bool:
    if num == 2 or num == 3:
        return True
    if (num % 2 == 0) or (num % int(num ** 0.5) == 0):
        return False
    for divisor in range(3, int(num ** 0.5), 2):
        if num % divisor == 0:
            return False
    return True

spiral_primes(15000)

