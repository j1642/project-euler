# Problem 54 - Poker Hands
# https://projecteuler.net/problem=54

# Lesson learned: Avoid comparing ints in strings form.

import urllib.request
from collections import Counter

@time_this
def poker_hand_win_count():
    '''For a set of poker hands, determine the number of times Player 1 beats
    Player 2.
    
    Assuming that there are no community cards, that all hands are valid, and
    that each hand has a clear winner.
    '''
    url = 'https://projecteuler.net/project/resources/p054_poker.txt'
    p1_hands = []
    p2_hands = []
    p1_win_count = 0
    
    with urllib.request.urlopen(url) as f:
        for line in f:
            line = line.decode()
            p1_hands.append(line[:15].strip().split(' '))
            p2_hands.append(line[15:].strip().split(' '))
            
    for ind, p1_hand in enumerate(p1_hands):
        p2_hand = p2_hands[ind]
        p1_hand_value = evaluate_hand(p1_hand).split(' ')
        p2_hand_value = evaluate_hand(p2_hand).split(' ')
        
        p1_hand_value = [int(num) for num in p1_hand_value]
        p2_hand_value = [int(num) for num in p2_hand_value]
        
        for ind, p1_val in enumerate(p1_hand_value):
            if p1_val > p2_hand_value[ind]:
                # Player 1 wins
                p1_win_count += 1
                break
            elif p1_val < p2_hand_value[ind]:
                # Player 2 wins
                break
            else:
                # Continue to get to tie-breakers
                continue
                
    return f'p1 wins: {p1_win_count}'
        
def evaluate_hand(hand: list):
    '''Returns value of hand, including tie-breaking kickers.
    
    Returned value is a space-separated string. The first integer represents
    overall hand strength, with following integers representing card values
    as shown below.
    
    Card values are represented by integers. For cards greater than 9:
    T: 10, J: 11, Q: 12, K: 13, and A: 14.
    
    8 X ----- Straight flush with X as the highest card
    7 X K --- Four of a kind of X, K kicker
    6 X Y --- Full house with trips of X and a pair of Y
    5 A B C D E - Flush with X as the highest card
    4 X Y --- Straight with X as the highest card
    3 X K --- Trips of X, K as kicker
    2 X Y K - Pair of X, pair of Y, K as kicker
    1 X K --- Pair of X, K as kicker
    0 A B C D E - High card X, next-highest card Y, third-highest card Z
    '''
    
    values = {'A': '14', 'K': '13', 'Q': '12', 'J': '11', 'T': '10'}
    flush = True
    straight = False
    four_of_a_kind = False
    full_house = False
    
    # Check for flush
    # The only use of card suits is the 'flush' boolean variable
    suits = []
    for card in hand:
        suits.append(card[1])
    for suit in suits:
        if suit == suits[0]:
            pass
        else:
            flush = False

    # Check for straight
    card_values = []
    straight_values = {'K': '13', 'Q': '12', 'J': '11', 'T': '10'}
    ace_count = 0
    
    for card in hand:
        if card[0].isdigit():
            card_values.append(card[0])
        elif card[0] in straight_values.keys():
            card_values.append(straight_values[card[0]])
        elif card[0] == 'A':
            ace_count += 1
    # '1' to check for low straights, '14' for high straights
    if '2' in card_values:
        for _ in range(ace_count):
            card_values.append('1')
    elif '13' in card_values:
        for _ in range(ace_count):
            card_values.append('14')
    # sort() method place '10' before '9'. Change to int to sort correctly.        
    card_values = [int(num) for num in card_values]
    card_values.sort()
    # Convert int to str for the join() method
    card_values = [str(num) for num in card_values]
    concat_values = ''.join(card_values)
    if concat_values in '1234567891011121314':
        straight = True
    
    
    # Clean up card_values variable before checking for pairs
    for _ in range(ace_count):
        if '1' in card_values:
            card_values.remove('1')
            card_values.append('14')
        else:
            # Add in aces which are not part of a straght
            # If '13' aka king is in card_values, then '14' is also already there
            if '13' not in card_values:
                card_values.append('14')
        #try:
         #   card_values.remove('1')
        #except ValueError:
         #   pass
    card_values = [int(num) for num in card_values]
    
    # Straight flush
    if straight and flush:
        return ' '.join(['8', highest_card(card_values)])
    
    
    # Check for pairs - full house, 4 of a kind, 3 of a kind, pair, two-pair.
    # If not 4 of a kind or full house, return flush or straight if appropriate.
    unique_values = set(card_values)
    counter = Counter(card_values)
    max_set = 0
    max_set_card = None
    lowest_pair = None
    for card in counter.keys():
        # Find most frequent, highest value card (max_set_card)
        # E.g. Four of a kind card in hand
        # E.g. Higher pair in a two pair hand
        # E.g. Highest card in flush or straight
        if counter[card] > max_set:
            max_set, max_set_card = counter[card], card
        elif counter[card] == max_set:
            # Revelant for sets (pairs, 3 of a kind, full house, 4 of a kind)
            if card > max_set_card and max_set > 1:
                lowest_pair, max_set_card = max_set_card, card
            # Relevant only for hands without any sets (pairs, etc.)
            elif card > max_set_card and max_set == 1:
                max_set_card = card

    # Following returns list of distinct card values        
    working_card_values = list(counter)
    working_card_values.remove(max_set_card)
    if lowest_pair != None:
        working_card_values.remove(lowest_pair)
    max_set_card = str(max_set_card)

    if len(unique_values) == 2:
        # Four of a kind or full house
        if max_set == 4:
            # Four of a kind
            # Kicker should be only remaining value in list
            kicker = working_card_values[0]
            return ' '.join(['7', max_set_card, str(kicker)])

        elif max_set == 3:
            # Full house
            # Pair card should be the only item in working_card_values
            pair_card = working_card_values[0]
            return ' '.join(['6', max_set_card, str(pair_card)])
        else:
            raise Exception('Neither if statement triggered in the \
            full house/4 of a kind block.')

    # Straight and flushes have priority over trips, two-pair, and one pair.
    elif straight or flush:
        # Flush has priority over straight
        if flush:
            second_highest = str(max(working_card_values))
            working_card_values.remove(int(second_highest))
            third_highest = str(max(working_card_values))
            working_card_values.remove(int(third_highest))
            fourth_highest = str(max(working_card_values))
            working_card_values.remove(int(fourth_highest))
            fifth_highest = str(working_card_values[0])
            return ' '.join(['5',
                             max_set_card,
                             second_highest,
                             third_highest,
                            fourth_highest,
                            fifth_highest])
        elif straight:
            if 2 and 14 in card_values:
                return ' '.join(['4', '5'])
            elif 13 and 14 in card_values:
                return ' '.join(['4', '14'])
            else:
                return ' '.join(['4', max_set_card])

    elif len(unique_values) == 3:
        # Trips or two-pair.
        if max_set == 3:
            # Trips (3 of a kind)
            kicker = highest_card(working_card_values)
            return ' '.join(['3', max_set_card, kicker])

        elif max_set == 2:
            # Two pair
            # One of the pairs is the max_set_card
            # Find lower value pair
            for card in counter.keys():
                if counter[card] == 2 and card != max_set_card:
                    second_pair_card = str(card)
            kicker = highest_card(working_card_values)
            return ' '.join(['2', max_set_card, str(lowest_pair), kicker])

        else:
            raise Exception('Neither if statement triggered in the trips/\
            two pair block.')

    elif len(unique_values) == 4:
        # One pair
        kicker = str(max(working_card_values))
        return ' '.join(['1', max_set_card, kicker])
    
    # If no other returns, return high card
    second_highest = str(max(working_card_values))
    working_card_values.remove(int(second_highest))
    third_highest = str(max(working_card_values))
    working_card_values.remove(int(third_highest))
    fourth_highest = str(max(working_card_values))
    working_card_values.remove(int(fourth_highest))
    fifth_highest = str(working_card_values[0])
    return ' '.join(['0',
                     max_set_card,
                     second_highest,
                     third_highest,
                    fourth_highest,
                    fifth_highest])


    
poker_hand_win_count()

