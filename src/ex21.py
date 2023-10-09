"""
Exercise 21 : Validate Date
"""



def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    from src.ex20 import is_leap_year

    # FIX : complete this
    if month not in range(0,13):
        return False
    if (is_leap_year(year) == True) and (month == 2 and day == 29):
        return True
    if (month in [1,3,5,7,8,10,12]) and (day in range(1,32)):
        return True
    elif (month in [4,6,9,11]) and (day in range(1,31)):
        return True
    elif (month == 2) and (day in range(1,29)):
        return True
    else:
        return False



