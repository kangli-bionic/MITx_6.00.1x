def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    flat_list = []

    for item in aList:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
            #for item2 in item:
            #    flat_list.append(item2)
        else:
            flat_list.append(item)

    return flat_list
