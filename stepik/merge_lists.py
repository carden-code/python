# Write a function merge (list1, list2) that takes two ascending sorted lists of integers as arguments
# and merges them into a single sorted list.
#
# Note 1. Lists list1 and list2 can be of different lengths.
def merge(list1, list2):
    return sorted(list1 + list2)


numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]
print(merge(numbers1, numbers2))
