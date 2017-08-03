'''
Defines a function to perform a Bubble Sort on a provided list.
sort(List) accepts a list as input and returns a new, sorted list.
sort_in_place(list) accepts a list as input and sorts the list itself.
'''

def sort_in_place(lst):
    '''
    Input - A list
    The list is then sorted in place
    '''

    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

def sort(lst):
    '''
    Input - A list
    Output - A new list that contains the sorted elements from input list
    '''
    new_lst = lst.copy()

    for i in range(0, len(new_lst)):
        for j in range(i+1, len(new_lst)):
            if new_lst[i] > new_lst[j]:
                new_lst[i], new_lst[j] = new_lst[j], new_lst[i]

    return new_lst

