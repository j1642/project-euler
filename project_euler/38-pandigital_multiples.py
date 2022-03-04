# Problem 38 - Pandigital Multiples
# https://projecteuler.net/problem=38

# Upper limit is a 4-digit number, because the concatenated products of a
#   5-digit number * 1 and * 2 would have at least 10 digits.

@time_this
def pandigital_multiples(max_range: int):
    '''Find largest 1-9 pandigital number formed by concatenated products of an
    integer and a set of integers 1, 2, ..., n.
    E.g. integer 1 multiplied by 1 through 9 gives 1, 2, 3, 4, 5, 6, 7, 8, 9
     -> 123456789.
    E.g. 192 multiplied by 1, 2, 3 gives 192, 384, 576 -> 192384576.
    '''
    pandigitals = []
    pandigital_19 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    
    for num in range(max_range):
        total_digits = 0
        pdts = []
        
        for factor in range(1, 10):
            pdt = num * factor
            pdts.append(str(pdt))

            total_digits += len(str(pdt))
            if total_digits < 9:
                continue
            else:
                break
        concatenated_pdts = ''.join(pdts)
        pdts_digits = list((concatenated_pdts))
        pdts_digits.sort()
        if pdts_digits == pandigital_19:
            pandigitals.append(int(concatenated_pdts))
        
    return max(pandigitals)
    

pandigital_multiples(9999)

