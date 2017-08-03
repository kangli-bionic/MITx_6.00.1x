def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    result_found = False
    exp = 0
    diff = abs((base ** exp) - num)

    while not result_found:
        exp += 1
        curr_diff = abs((base ** exp) - num)
        if curr_diff < diff:
            diff = curr_diff
        else:
            return exp-1
