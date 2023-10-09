"""
Exercise 18 : Buy 8 get 1 free
"""


def get_cost_of_coffee(num, price):
    #FIX
    if num > 8:
        discount = num//8
        total = price*num - discount*price
        return total
    else:
        return num*price

def get_cost_of_coffee_2(num, price):
    #FIX
    if num > 8:
        discount = num//8
        total = price*num - discount*price
        return total
    else:
        return num*price