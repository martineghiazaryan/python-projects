import random
import time

# Implementing binary search algorithm !!
# Showing that binary search is way faster than the simple naive search in a sorted list

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


def binary_search(l, target, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(l) - 1

    if high < low:
        return -1

    mid_point = (low + high) // 2
    if l[mid_point] == target:
        return mid_point
    elif l[mid_point] > target:
        return binary_search(l, target, low, mid_point - 1)
    else:
        return binary_search(l, target, mid_point + 1, high)


if __name__ == '__main__':
    # l = [0,25,38,98,158,241]
    # print(naive_search(l, 158))
    # print(binary_search(l, 158))

    length = 10000
    sorted_list = set()

    while (len(sorted_list) < length):
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    # start = time.time()
    # for target in sorted_list:
    #     naive_search(sorted_list, target)
    # end = time.time()
    # print('Naive search time is ', (end - start)/length, 'seconds')

    
    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print('Binary search time is ', (end - start)/length, 'seconds')