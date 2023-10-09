"""
Exercise 14
"""


def average(num_list: list) -> float:
    """
    Calculate the average of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - float: The average of the numbers in the list.
      If the list is empty, returns 0.
    """
    #FIX
    sum_result = 0
    for i in num_list:
        sum_result += i
    if sum_result > 0:
        return sum_result/len(num_list)
    else:
        return 0