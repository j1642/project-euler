# Problem 40 - Champernowe's Constant
# https://projecteuler.net/problem=40

# Hold all numbers in list to save processing time at expense of memory.
# List isn't incredibly large so not a big deal here.

@time_this
def champernowe():
    '''Find product of 1st, 10th, 100th, 1,000th, 10,000th, 100,000th, and
    1,000,000th decimal digit of Champernowne's constant.'''
    champ = ['0.']
    
    for num in range(1, 186000):
        champ.append(str(num))
    champ = ''.join(champ)
        
    assert len(champ) > 1000001
    
    # First decimal in string has index 2, 10th decimal has index 11, etc.
    indexes = [2, 11, 101, 1001, 10001, 100001, 1000001]
    product = 1
    for index in indexes:
        product *= int(champ[index])
        
    return product
    
champernowe()

