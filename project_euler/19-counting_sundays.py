# Problem 19 - Counting Sundays on 1st of the month
# https://projecteuler.net/problem=19
# Could use datetime module instead. This way seemed interesting as well.
@time_this
def count_sundays():
    '''Count Sundays that fell on first of the month.
    
    The date variable is in day/month/year format.
    The day_of_week variable ranges from 1-7, Monday to Sunday.'''
    
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                     9: 30, 10: 31, 11: 30, 12: 31}
    leap_year = False
    date = [1, 1, 1901]
    end = [31, 12, 2000]
    day_of_week = 2
    count = 0
    
    while date != end:
        # Check if it is the first of the month and a Sunday
        if date[0] == 1 and day_of_week == 7:
            count += 1
        date[0] += 1
        day_of_week += 1
        # Check if it is the beginning of a new week
        # If so, set day to Monday
        if day_of_week == 8:
            day_of_week = 1
        # Check if it is the start of the next month
        if date[0] > days_in_month[date[1]]:
            date[0], date[1] = 1, date[1] + 1
            # Check if it is the start of the next year
            if date[1] == 13:
                date[1], date[2] = 1, date[2] + 1
                # Check if it is a leap year
                if date[2] % 4 == 0:
                    leap_year = True
                    days_in_month[2] = 29
                else:
                    leap_year = False
                    days_in_month[2] = 28
    
    return count

count_sundays()
