"""
Exercise 20 : Leap Year
"""


def is_leap_year(year):
    """
    Check if the given year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if the year is a leap year, False otherwise.
    """
    # FIX : complete this
    return  ((year%4 == 0) and (year%100 != 0)) or ((year%4 == 0) and (year%100 == 0) and ((year%400 == 0)))
