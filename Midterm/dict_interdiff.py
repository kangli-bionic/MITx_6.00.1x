def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''

    dict_inter = {}
    dict_diff = {}

    for key in d1:
        if key in d2:
            dict_inter[key] = f(d1[key], d2[key])

    for key in d1:
        if key not in d2:
            dict_diff[key] = d1[key]

    for key in d2:
        if key not in d1:
            dict_diff[key] = d2[key]

    return dict_inter, dict_diff

def f(a, b):
    return a > b

