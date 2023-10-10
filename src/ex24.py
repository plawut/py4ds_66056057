"""
Exercise 24 : Every 15 minutes, ante meridiem (am) and post meridiem (pm)
ante : before
post : after
meridiem : midday
"""


def get_time_every_15_min():
    """
    Generate a time string every 15 minutes.

    This function iterates through the meridiems, hours, and minutes to generate a time string
    for every 15 minutes. It prints the time string in the format "hour:minute meridiem".

    Returns:
        str: The generated time string.
    """
    # FIX : complete this
    hour_list = [12,1,2,3,4,5,6,7,8,9,10,11]
    for i in ['am','pm']:
        if i == 'am':
            for j in hour_list:
                for k in range(0,46,15):
                    if k == 0:
                        print(f'{j}:{k}0 {i}')
                    else:
                        print(f'{j}:{k} {i}')
        else:
            for j in hour_list:
                for k in range(0,46,15):
                    if k == 0:
                        print(f'{j}:{k}0 {i}')
                    else:
                        print(f'{j}:{k} {i}')


