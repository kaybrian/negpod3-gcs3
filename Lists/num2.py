#!/usr/bin/python3

'''
Write a python function that takes as parameters a list of 
integers and a target value, it sorts the list in ascending order 
and returns the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

'''
nums = [1, 3, 5, 6]
target = 5


def find_index_of_target(nums, target):
    sorted_list = sorted(nums)
    if target in sorted_list:
        return sorted_list.index(target)
    else:
        pass


result = find_index_of_target(nums, target)
print(result)
