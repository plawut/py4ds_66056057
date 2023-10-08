"""
Execise 6
"""


def ordinal_suffix(num):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # FIX : complete this
    if (num >= 10 and num <= 20):
        return str(num)+'th'
    else:
        num = str(num)
        if num[-1] == '1':
            return num+'st'
        elif num[-1] == '2':
            return num+'nd'
        elif num[-1] == '3':
            return num+'rd'
        else:
            return num+'th'

#%%
