def polysum(n, s):
    '''
    Inputs:
        n = Number of sides in the regular polygon
        s = unit length of each side
    Output:
        Function returns the sum of the Area and the Square of the
        perimeter of the polygon
    '''
    #Importing the standard library math to provide the Tan function and pi
    import math

    #Calculate the area using the formula provided
    area = (0.25 * n * s**2)/(math.tan(math.pi/n))

    '''Calculate the square of the perimeter by adding the sides together and
    squaring it'''
    peri_square = (n * s) ** 2

    #Returning the result after rounding to 4 digits by using the round builtin
    return round((area + peri_square), 4)

