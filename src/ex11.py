"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    #FIX
    if tsec < 60:
        return str(tsec)+'s'
    elif (tsec >= 60) and (tsec < 3600):
        x = tsec//60
        y = tsec%60
        if y != 0:
            return str(x)+'m'+' '+str(y)+'s'
        else:
            return str(x)+'m'
    else:
        a = tsec//3600
        b = tsec%3600
        if b > 60:
            c = b//60
            d = b%60
            return str(a)+'h' + ' ' + str(c)+'m' + ' ' + str(d) + 's'
        elif (b>0) and (b<=60):
            return str(a)+'h' + ' ' + str(b) + 's'
        else:
            return str(a)+'h'

