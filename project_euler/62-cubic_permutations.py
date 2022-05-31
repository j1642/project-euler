# Problem 62 - Cubic Permutations
# https://projecteuler.net/problem=62

# This is another question where it is vital to avoid combinatorial explosion.
# Generating a set of cubes and examining their permutations is too expensive.

from collections import defaultdict

@time_this
def permute_cube_digits():
    '''Find the smallest cube for which exactly five permutations of its digits
    are also cubes.
    '''
    cubes = []
    sorted_cube_repetition_count = defaultdict(int)
    n = 0
    while True:
        n += 1
        cube = str(n ** 3)
        cubes.append(cube)
        sorted_cube = sorted(cube)
        sorted_cube = ''.join(sorted_cube)
        sorted_cube_repetition_count[sorted_cube] += 1
        # Searching for 5 permutations which are all cubes.
        if sorted_cube_repetition_count[sorted_cube] == 5:
            cubic_permutations = []
            for old_cube in cubes:
                assert isinstance(sorted(old_cube), list)
                assert isinstance(sorted(cube), list)
                # Compare list to list. Careful with types.
                if sorted(old_cube) == sorted(cube):
                    cubic_permutations.append(old_cube)
                    
            return sorted_cube, min(cubic_permutations)
        
        
permute_cube_digits()
