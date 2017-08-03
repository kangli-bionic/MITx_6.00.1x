def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    list_biggest = []
    biggest_len = 0

    for element in aDict:
        if isinstance(aDict[element], (dict, list, tuple)):
            current_len = len(aDict[element])
        else:
            current_len = 1
        if current_len > biggest_len:
            list_biggest = [element]
            biggest_len = current_len
        elif current_len == biggest_len:
            list_biggest.append(element)
            biggest_len = current_len

    return list_biggest
