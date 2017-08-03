def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        if aStr[:] == char:
            return True
        else:
            return False

    midChar = aStr[round(len(aStr)/2)]

    if char == midChar:
        return True
    elif char < midChar:
        return isIn(char, aStr[0:round(len(aStr)/2)])
    elif char > midChar:
        return isIn(char, aStr[round(len(aStr)/2):])
