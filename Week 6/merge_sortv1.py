'''
Defines a function to perform a Merge Sort on a provided list.
sort(List) accepts a list as input and returns a new, sorted list.
sort_in_place(list) accepts a list as input and sorts the list itself.
'''

def sort_in_place(lst):
    '''
    Input - A list
    The list is then sorted in place
    '''
    lst[:] = merge_func(lst)

def sort(lst):
    '''
    Input - A list
    Output - A new list that contains the sorted elements from input list
    '''
    return merge_func(lst)

def merge_func(lst):
    '''
    The actual procedure that performs merge sort
    '''
    if len(lst) == 1:
        return lst
    else:
        upper = merge_func(lst[:len(lst)//2])
        lower = merge_func(lst[len(lst)//2:])
        return merge(upper, lower)

def merge(lst1, lst2):
    '''
    Input - Two sorted lists
    Action - Merge lst1 into lst2 to created a sorted lst3
    Caveat - Returns new list lst3
    '''
    lst3 = []

    while lst1 or lst2:
        if not lst1:
            while lst2:
                lst3.append(lst2.pop(0))
        elif not lst2:
            while lst1:
                lst3.append(lst1.pop(0))
        else:
            if lst1[0] < lst2[0]:
                lst3.append(lst1.pop(0))
            else:
                lst3.append(lst2.pop(0))

    return lst3


