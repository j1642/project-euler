# Problem 22 - Names scores
# https://projecteuler.net/problem=22
import string
import urllib.request

@time_this
def names_scores():
    letters = {}
    for ind, letter in enumerate(string.ascii_uppercase):
        letters[letter] = ind + 1
    
    with urllib.request.urlopen(
        'https://projecteuler.net/project/resources/p022_names.txt') as site:
        text = site.read().decode()
        names = text.split(',')
        names = sorted(names)
        
        sum_scores = 0
        for ind, name in enumerate(names):
            score = 0
            name = name.strip('\"')
            for letter in name:
                score += letters[letter]
            score *= (ind + 1)
            sum_scores += score
            
        return sum_scores
        

names_scores()
