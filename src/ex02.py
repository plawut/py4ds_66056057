"""
Execise 2
"""


def convert_to_fahrenheit(Celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # FIX : complete this
    result = (9/5) * Celsius + 32
    return  result


def convert_to_celsius(Fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # FIX : complete this
    result = (Fahrenheit - 32) * (5/9)
    return result