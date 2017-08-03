def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0

    for i, j in zip(listA, listB):
        result += i * j

    return result
