"""
Exercise 15
"""


def median(num_list):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    #FIX
    if num_list == []:
        return  None
    elif len(num_list) % 2 != 0:
        num_list.sort()
        med_posit = len(num_list)//2
        return num_list[med_posit]
    else:
        num_list.sort()
        med_posit_1 = len(num_list)//2
        med_posit_2 = med_posit_1 - 1
        return (num_list[med_posit_1] + num_list[med_posit_2])/2

