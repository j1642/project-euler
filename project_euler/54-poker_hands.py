# Problem 54 - Poker Hands
# https://projecteuler.net/problem=54

# Lesson learned: Avoid comparing ints in string form.

# TODO: Refactor as class for testing? Nested functions cannot be tested easily

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

    with urllib.request.urlopen(url) as response:
        for line in response:
            line = line.decode()
            p1_hands.append(line[:15].strip().split(' '))
            p2_hands.append(line[15:].strip().split(' '))

    for i, p1_hand in enumerate(p1_hands):
        p2_hand = p2_hands[i]
        p1_hand_value = evaluate_hand(p1_hand)
        p2_hand_value = evaluate_hand(p2_hand)

        for j, p1_val in enumerate(p1_hand_value):
            p2_val = p2_hand_value[j]
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

    return p1_win_count


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
    5 A B C D E - Flush with A as the highest card
    4 X ----- Straight with X as the highest card
    3 X A B - Trips (3-of-a-kind) of X. A and B tie-breakers
    2 X Y 13 - Higher pair of X, lower pair of Y, K as kicker
    1 X A B C - Pair of X. A, B, and C as tie-breakers
    0 A B C D E - High card A, next-highest card B, third-highest card C, etc.
    '''

    def is_flush(hand: list) -> bool:
        '''Input format example: ['8C', 'TS', 'KC', '9H', '4S']
        '''
        suit = hand[0][1]
        for card in hand:
            if suit != card[1]:
                return False
        return True


    def change_card_str_to_int(hand_as_strs: list) -> list:
        '''Input format example: ['8C', 'TS', 'KC', '9H', '4S']
        Output: [8, 10, 13, 9, 4]
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
        card_values_copy = card_values.copy()
        # Append 1 to check for low straights.
        if 14 in card_values_copy:
            if 2 in card_values_copy:
                card_values_copy.append(0)
        cards_as_str_for_is_straight = [str(num) for num in card_values_copy]
        concat_values = ''.join(cards_as_str_for_is_straight)
        # Card values were sorted in change_card_str_to_int().
        if concat_values in '1234567891011121314':
            return True
        return False



    def check_for_pairs(cards_as_int: list) -> tuple:
        '''Input  example: [14, 5, 9, 10, 11]
        Output: tuple(int, int, int)
        '''
        # Check for pairs (full house, 4 of a kind, 3 of a kind, pair, 2-pair).
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

        return (most_frequent_card, most_freq_card_count, lowest_pair)


    def return_4_of_a_kind_or_full_house():
        # Four of a kind or full house
        if most_freq_card_count == 4:
            # Four of a kind
            # Kicker should be only remaining value in list
            kicker = distinct_cards_as_int.pop()
            assert not distinct_cards_as_int

            return [7, most_frequent_card, kicker]

        elif most_freq_card_count == 3:
            # Full house
            # Pair card should be the only item in distinct_cards_as_int
            pair_card = distinct_cards_as_int.pop()
            assert not distinct_cards_as_int

            return [6, most_frequent_card, pair_card]
        else:
            raise Exception('Neither if statement triggered in the '
            'full house/4 of a kind block.')

    def return_flush():
        flush_result = [5, most_frequent_card]
        # Because distinct_cards_as_int is sorted, we can repeatedly pop.
        # the maximum value in the list.
        # Range must be 4 b/c one card is already accounted for (therefore
        # range is not 5) and there can be no pairs in a flush.
        for _ in range(4):
            max_card = distinct_cards_as_int.pop()
            flush_result.append(max_card)
        assert not distinct_cards_as_int

        return flush_result

    def return_straight():
        if 14 in cards_as_int:
            # Low straight
            if 2 in cards_as_int:
                # A straight with a 2 and an ace will be an ace to 5 straight.
                return [4, 5]
            # High straight
            elif 13 in cards_as_int:
                return [4, 14]
        else:
            # Middling straight
            return [4, most_frequent_card]


    def return_3_of_a_kind_or_2_pair():
        if most_freq_card_count == 3:
            # Trips (3 of a kind)
            trips_result = [3, most_frequent_card]
            # Two unpaired cards in the hand and in distinct_cards_as_int.
            for _ in range(2):
                high_card = distinct_cards_as_int.pop()
                trips_result.append(high_card)
            assert not distinct_cards_as_int

            return trips_result

        elif most_freq_card_count == 2:
            # Two pair
            kicker = distinct_cards_as_int.pop()
            assert not distinct_cards_as_int

            return [2, most_frequent_card, lowest_pair, kicker]

        else:
            raise Exception('Neither if statement triggered in the \
            "elif len(unique_values) == 3" block.')


    def return_one_pair():
        one_pair_result = [1, most_frequent_card]
        # Three unpaird cards in the hand and distinct_cards_as_int.
        for _ in range(3):
            high_card = distinct_cards_as_int.pop()
            one_pair_result.append(high_card)
        assert not distinct_cards_as_int

        return one_pair_result


    def return_high_card():
        high_card_result = [0, most_frequent_card]
        # There are 4 cards unaccounted for and there can be no pairs. Therefore,
        # range has an argument of 4.
        #print(distinct_cards_as_int, most_frequent_card, LEN_UNIQUE_CARD_VALUES)
        for _ in range(4):
            max_card = distinct_cards_as_int.pop()
            high_card_result.append(max_card)
        assert not distinct_cards_as_int

        return high_card_result


    cards_as_int = change_card_str_to_int(hand)
    STRAIGHT = is_straight(cards_as_int)
    FLUSH = is_flush(hand)

    # Straight flush, the best hand. If true, no further computation needed.
    if STRAIGHT and FLUSH:
        # cards_as_int is sorted immediately after it is created.
        return [8, cards_as_int[-1]]

    most_frequent_card, most_freq_card_count, lowest_pair = \
        check_for_pairs(cards_as_int)


    # Following returns list of distinct card values
    distinct_cards_as_int = list(set(cards_as_int))
    LEN_UNIQUE_CARD_VALUES = len(distinct_cards_as_int)
    distinct_cards_as_int.sort()
    distinct_cards_as_int.remove(most_frequent_card)
    # The linter doesn't like "lowest_pair != None", and the terminal doesn't
    # like "x is not None" where x is an integer.
    if lowest_pair != None:
        distinct_cards_as_int.remove(lowest_pair)



    if LEN_UNIQUE_CARD_VALUES == 2:
        return return_4_of_a_kind_or_full_house()

    # Straight and flushes have priority over trips, two-pair, and one pair.
    elif STRAIGHT or FLUSH:
        # A flush has priority over a straight due to its higher value.
        if FLUSH:
            return return_flush()
        elif STRAIGHT:
            return return_straight()

    elif LEN_UNIQUE_CARD_VALUES == 3:
        # Trips (3-of-a-kind) or two-pair.
        return return_3_of_a_kind_or_2_pair()


    elif LEN_UNIQUE_CARD_VALUES == 4:
        # One pair
        return return_one_pair()

    else:
        # If no other returns, only high card remains. Lowest value hand.
        return return_high_card()



if __name__ == '__main__':
    import unittest
    
    class Testing123(unittest.TestCase):
        def test_answer(self):
            answer = poker_hand_win_count()
            self.assertEqual(answer, 376)
            #self.assertTrue(poker_hand_win_count.is_straight([2,3,4,5,14]))
    
    unittest.main()
