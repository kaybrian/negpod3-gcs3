#!/usr/bin/python3
'''
Write a python function that takes a list of integer nums and an integer target, 
and returns indices of the two numbers such that they add up to the target. 
Return the indices in a tuple. You may assume that each input would have exactly
one solution, and you may not use the same element twice.
'''

nums = [1,2,5,7,8]

target = 3

def twoSum(nums, target):
    prevMap = {}
    for index, num in enumerate(nums):
        diff = target - num
        if diff in prevMap:
            return [prevMap[diff], index]
        prevMap[num] = index
    return


result = twoSum(nums, target)
print(result)
