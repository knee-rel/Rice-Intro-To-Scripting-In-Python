"""
Project for Week 4 of "Python Programming Essentials".
Collection of functions to process dates.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import datetime

def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    if month == 4 or month == 6 or month == 9 or month == 11:
        return int(30)
    elif month == 1 or month == 3 or month == 5:
        return int(31)
    elif month == 7 or month == 8 or month == 10 or month == 12:
        return int(31)
    else:
        return int(28)

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """

    days = days_in_month(year, month)
    if (datetime.MINYEAR <= year <= datetime.MAXYEAR):
        if (month >= 1 and month <= 12):
            if(day >= 1 and day <= days):
                return True
            else:
                return False
        return False
    return False

print('Unit test ', is_valid_date(200000, 1, 1))

def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """

    if is_valid_date(year1, month1, day1) is False or is_valid_date(year2, month2, day2) is False:
        return 0
    elif datetime.date(year1, month1, day1) > datetime.date(year2, month2, day2):
        return 0
    else: 
        return (datetime.date(year2, month2, day2) - datetime.date(year1, month1, day1)).days

print('Unit test ', days_between(2016, 5, 7, 2016, 5, 9))

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    if is_valid_date(year, month, day) is False:
        return 0 
    elif datetime.date.today() < datetime.date(year, month, day):
        return 0
    else:
        return (datetime.date.today() - datetime.date(year, month, day)).days
print('Unit test ', age_in_days(2015, 11, 1))