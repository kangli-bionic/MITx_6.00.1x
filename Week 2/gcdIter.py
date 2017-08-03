def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = 1
    for i in range(1, max(a, b)):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

print(gcdIter(15, 25))
