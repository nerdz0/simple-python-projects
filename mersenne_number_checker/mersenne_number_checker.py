"""
----------------------
Mersenne Number Checker
-----------------------

This module provides a simple beginner friendly function to check 
whether a given integer is a Mersenne number.

A Mersenne number is a number that can be written in the form:

    M = 2^p - 1

where `p` is a positive integer.

Examples of Mersenne numbers:
    3   = 2^2 - 1
    7   = 2^3 - 1
    31  = 2^5 - 1
    127 = 2^7 - 1

The algorithm used here works by checking whether (number + 1) can be
repeatedly divided by 2 until it reaches 1. If it can, then the number
is a Mersenne number.
"""


def mersenne_number_checker(number : int) -> bool:
    """
    Check whether a given number is a Mersenne number.

    The function adds 1 to the given number and repeatedly divides
    the result by 2. If the number can be reduced to 1 through
    exact divisions by 2, then the original number is a Mersenne number.

    Parameters
    ----------
    number : int
        The integer that needs to be checked.

    Returns
    -------
    bool
        True  -> if the number is a Mersenne number
        False -> if the number is not a Mersenne number
    """

    # Add 1 to the input number
    # If the number is a Mersenne number, (number + 1) will be a power of 2
    value = number + 1

    # Counter used to track successful divisions by 2
    b = 0

    # Loop indefinetely until a stop condition is reached 
    while True:

        # If the value becomes 1 or less, stop the loop
        if value == 1 or value <= 1:
            break
        
        # Divide the value by 2
        value = value / 2
        
        # Check if the result is still an integer 
        if value.is_integer():

            # On successful division add 1 to b
            b = b + 1

        else:
            # If the division produces a non integer,
            # reset the counter since it's not a clean power of 2 
            b = 0 

    # If we had at least one successful clean division,
    # the number behaves like a Mersenne number 
    if b > 0:
        return True

    # Otherwise it is not a Mersenne number  
    else:
        return False

'''
-------------------
Program Entry Point
-------------------
'''

# Take input from the user 
user_input = int(input(":: Enter desired number >>> "))

# Call the function and print the result 
print(mersenne_number_checker(user_input))