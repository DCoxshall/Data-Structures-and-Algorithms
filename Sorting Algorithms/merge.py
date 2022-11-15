import random


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        split = int(len(arr) / 2)
        l = arr[0:split]
        r = arr[split:]
        return merge(merge_sort(l), merge_sort(r))


def merge(left, right):
    new = []
    while left != [] and right != []:
        if left[0] < right[0]:
            new.append(left[0])
            left = left[1:]
        else:
            new.append(right[0])
            right = right[1:]
    new += left + right
    return new


unsorted = []
for i in range(10000):
    unsorted.append(random.randint(0, 100))
merge_sort(unsorted)
