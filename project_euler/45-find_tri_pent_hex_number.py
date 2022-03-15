# Problm 45 - Triangluar, Pentagonal, and Hexagonal
# https://projecteuler.net/problem=45

@time_this
def find_tri_pent_hex_num(max_range: int):
    '''Find the next number, after 40755, which is triangluar, pentagonal, and
    hexagonal.
    '''
    hex_nums = []
    
    # The lowest tri., pent., and hex. numbers are all one, not zero.
    for n in range(1, max_range):
        hex_nums.append(n * (2 * n - 1))
        
    # Iterate through hexagonal numbers because they are the most exclusive,
    #   in that they are the most separated from each other on a number line.
    # Iterating through one of the others would have more fruitless calculations.
    for n in hex_nums:
        if n > 40755:
            pentag_test = ((24 * n + 1) ** 0.5 + 1) / 6
            tri_test = ((8 * n + 1) ** 0.5 - 1) / 2
            if pentag_test == int(pentag_test) and tri_test == int(tri_test):
                return n
        

find_tri_pent_hex_num(200000)

