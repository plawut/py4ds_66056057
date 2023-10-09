"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    #FIX
    check = []
    for i in num_list:
        if i not in check:
            check.append(i)
        else:
            return i

