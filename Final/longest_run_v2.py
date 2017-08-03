'''MITx Final Exam problem'''

def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing.
    In case of a tie for the longest run, choose the longest run
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run.
    """

    prev_num = L[0]
    current_sum = L[0]
    longest_sum = 0
    long_run = 0
    current_run = 1
    #current_dir is 0 for decreasing and 1 for increasing
    current_dir = 0
    flat_length = 1
    print('num, current_dir, current_run, current_sum, long_run, longest_sum')

    for num in L[1:]:
        if current_dir == 0:
            if num <= prev_num:
                if num == prev_num:
                    flat_length += 1
                else:
                    flat_length = 1
                current_sum += num
                current_run += 1
                prev_num = num
            else:
                if current_run > long_run:
                    long_run = current_run
                    longest_sum = current_sum
                    current_run = 2 + flat_length
                    current_sum = prev_num*flat_length + num
                    prev_num = num
                    current_dir = 1
                else:
                    current_run = 2 + flat_length
                    current_sum = prev_num*flat_length + num
                    prev_num = num
                    current_dir = 1

        else:
            if num >= prev_num:
                if num == prev_num:
                    flat_length += 1
                else:
                    flat_length = 1
                current_sum += num
                current_run += 1
                prev_num = num
            else:
                if current_run > long_run:
                    long_run = current_run
                    longest_sum = current_sum
                    current_run = 2 + flat_length
                    current_sum = prev_num*flat_length + num
                    prev_num = num
                    current_dir = 0
                else:
                    current_run = 2 + flat_length
                    current_sum = prev_num*flat_length + num
                    prev_num = num
                    current_dir = 0
        print(num, current_dir, current_run, current_sum, long_run, longest_sum)

    if long_run < current_run:
        return current_sum

    return longest_sum

