def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        gcd = gcdRecur(b, a % b)
    return gcd

print(gcdRecur(6, 12))


