# Problem 54 - Poker Hands
# https://projecteuler.net/problem=54

# Lesson learned: Avoid comparing ints in string form.

# TODO: Break into smaller functions so this can be showed off.
# TODO: Add tests.
# TODO: Use the linter.

import urllib.request
from collections import Counter

#@time_this
def poker_hand_win_count():
    '''For a set of poker hands, determine the number of times Player 1 beats
    Player 2.
    
    Assume there are no community cards, that all hands are valid, and
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
        p1_hand_value = evaluate_hand(p1_hand)
        p2_hand_value = evaluate_hand(p2_hand)
        
        for ind, p1_val in enumerate(p1_hand_value):
            p2_val = p2_hand_value[ind]
            if p1_val > p2_val:
            # Player 1 wins
                p1_win_count += 1
                break
            elif p1_val < p2_val:
                # Player 2 wins
                break
            else:
                # Continue to get to tie-breakers
                continue
            
                
    return f'p1 wins: {p1_win_count}'
        
def evaluate_hand(hand: list) -> list:
    '''Returns value of hand, including tie-breaking kickers.
    
    Returned value is a list of int. The first integer represents
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
    
    def is_flush(hand: list) -> bool:
        '''Input format example: ['8C', 'TS', 'KC', '9H', '4S']
        '''
        suit = hand[0][1]
        for card in hand:
            if suit == card[1]:
                continue
            else:
                return False
        return True
    
    
    def change_card_str_to_int(hand_as_strs: list) -> list:
        '''Input format example: ['8C', 'TS', 'KC', '9H', '4S']
        '''
        CARD_VALUES = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
        cards_as_int = []
        for card in hand_as_strs:
            try:
                cards_as_int.append(CARD_VALUES[card[0]])
            except KeyError:
                cards_as_int.append(int(card[0]))
                continue
                
        cards_as_int.sort()
            
        return cards_as_int
    
    
    def is_straight(card_values: list) -> bool:
        '''Input example: [3, 14, 5, 10, 12]
        '''
        # Caution: Copy card_values parameter to another variable to avoid
        # any appended 1s from bleeding out of this scope.
        card_values_copy = card_values
        # Append 1 to check for low straights.
        if 14 in card_values_copy:        
            if 2 in card_values_copy:
                card_values_copy.append(0)
        cards_as_str_for_is_straight = [str(num) for num in card_values_copy]
        concat_values = ''.join(cards_as_str_for_is_straight)
        # Card values were sorted in change_card_str_to_int().
        if concat_values in '1234567891011121314':
            return True
        else:
            return False
    
    cards_as_int = change_card_str_to_int(hand)
    # Must use copy method here or iteratively append values to new list.
    # Assigning cards_as_int to another variable leads to scope bleeding
    # from inside is_straight().
    cards_as_int_copy = cards_as_int.copy()
    FLUSH = is_flush(hand)
    STRAIGHT = is_straight(cards_as_int_copy)
    four_of_a_kind = False
    full_house = False
    

    
    # Straight flush, the best hand.
    if STRAIGHT and FLUSH:
        return [8, max(cards_as_int)]
    
    
    # Check for pairs - full house, 4 of a kind, 3 of a kind, pair, two-pair.
    # If not 4 of a kind or full house, return flush or straight if appropriate.
    unique_values = set(cards_as_int)
    counter = Counter(cards_as_int)
    most_frequent_card = 0
    most_freq_card_count = 0
    lowest_pair = None
    # Equivalent to iterating through counter.keys()
    for card in counter:
        # Find most frequent, highest value card (most_frequent_card)
        # E.g. Four of a kind card in hand
        # E.g. Higher pair in a two pair hand
        # E.g. Highest card in flush or straight
        if counter[card] > most_freq_card_count:
            most_freq_card_count, most_frequent_card = counter[card], card
        elif counter[card] == most_freq_card_count:
            # Revelant for sets (pairs, 3 of a kind, full house, 4 of a kind)
            if card > most_frequent_card and most_freq_card_count > 1:
                lowest_pair, most_frequent_card = most_frequent_card, card
            # Relevant only for hands without any sets (pairs, etc.)
            elif card > most_frequent_card and most_freq_card_count == 1:
                most_frequent_card = card

    # Following returns list of distinct card values        
    working_card_values = list(counter)
    working_card_values.sort()
    working_card_values.remove(most_frequent_card)
    if lowest_pair != None:
        working_card_values.remove(lowest_pair)

    if len(unique_values) == 2:
        # Four of a kind or full house
        if most_freq_card_count == 4:
            # Four of a kind
            # Kicker should be only remaining value in list
            kicker = working_card_values[0]
            return [7, most_frequent_card, kicker]

        elif most_freq_card_count == 3:
            # Full house
            # Pair card should be the only item in working_card_values
            pair_card = working_card_values[0]
            return [6, most_frequent_card, pair_card]
        else:
            raise Exception('Neither if statement triggered in the '
            'full house/4 of a kind block.')

    # Straight and flushes have priority over trips, two-pair, and one pair.
    elif STRAIGHT or FLUSH:
        # A flush has priority over a straight due to its higher value.
        if FLUSH:
            flush_result = [5, most_frequent_card]
            # Because working_card_values is sorted, we can repeatedly pop.
            # the maximum value in the list.
            # Range must be 4 b/c one card is already accounted for (therefore
            # range is not 5) and there can be no pairs in a flush.
            for _ in range(4):
                max_card = working_card_values.pop()
                flush_result.append(max_card)
            assert not working_card_values

            return flush_result 
            
        elif STRAIGHT:
            # Low flush
            if 2 and 14 in cards_as_int:
                return [4, 5]
            # High flush
            elif 13 and 14 in cards_as_int:
                return [4, 14]
            else:
                return [4, most_frequent_card]

    elif len(unique_values) == 3:
        # Trips (3-of-a-kind) or two-pair
        if most_freq_card_count == 3:
            # Trips (3 of a kind)
            kicker = max(working_card_values)
            return [3, most_frequent_card, kicker]

        elif most_freq_card_count == 2:
            # Two pair
            # One of the pairs is most_frequent_card
            # Find lower value pair
            for card in counter:
                if counter[card] == 2 and card != most_frequent_card:
                    second_pair_card = card
            kicker = max(working_card_values)
            return [2, most_frequent_card, lowest_pair, kicker]

        else:
            raise Exception('Neither if statement triggered in the \
            "elif len(unique_values) == 3" block.')

    elif len(unique_values) == 4:
        # One pair
        kicker = max(working_card_values)
        return [1, most_frequent_card, kicker]
    
    # If no other returns, return high card
    high_card_result = [0, most_frequent_card]
    # There are 4 cards unaccounted for and there can be no pairs. Therefore,
    # range has an argument of 4.
    for _ in range(4):
        max_card = working_card_values.pop()
        high_card_result.append(max_card)
    assert not working_card_values

    return high_card_result


    
print(poker_hand_win_count())

