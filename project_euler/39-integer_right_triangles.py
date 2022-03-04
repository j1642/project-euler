# Problem 39 - Integer Right Triangles
# https://projecteuler.net/problem=39

# Find maximum amount of pythagorean triples.
# Big speed improvements can come from order of checks in "if a and b and c:"
# If b = 0, perim = a + b + sqrt(a^2 + b^2) = 2a, so a <= max_perimeter / 2

# Remove perimeter for loop, unncessary to set perimeter and work from it.
from collections import defaultdict

@time_this
def integer_right_triangles(max_perimeter):
    '''Find maximum amount of side length combinations (pythagorean triples)
    for a right triangle with a perimeter of an integer value less than or equal
    to 1000.
    E.g. for perimemter of 120, there are three side length combinations.'''
    
    
    triples_count = defaultdict(int)
    # Side A as a, side B as b
    # Only one base (A or B) has to search high lengths.
    for a in range(1, max_perimeter // 2 + 1):
        for b in range(a, max_perimeter // 2 + 1):
            c_squared = a * a + b * b
            c = c_squared ** 0.5
            # Check if c^2 is a valid square.
            # sqrt(c^2) would have decimals and wouln't equal perimeter.
            if (a + b + c <= max_perimeter) and (int(c) == c):
                triples_count[int(a + b + c)] += 1
                
    return max(triples_count, key=triples_count.get)
        

integer_right_triangles(1000)

