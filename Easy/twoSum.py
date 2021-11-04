# -*- coding: utf-8 -*-
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].


"""
# def twoSum(self, nums: List[int], target: int) -> List[int]:

"""
# Solucion mia
class Solution:
    def twoSum(nums, target):
        nums_copy = nums.copy()
        i = True
        iteration = 0
        while(i):
            missing = target - nums_copy.pop(0)
            if missing in nums_copy:
                position = nums_copy.index(missing) + iteration + 1
                return[iteration, position]
            if not nums_copy:
                i = False
            iteration += 1
        return[]
"""
# """
# Solucion de un pro:


class Solution:
    def twoSum(nums, target):
        dictionary = {}
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
            dictionary.update({nums[i]: i})
# """

# %% Main program


nums = [1, 2, 3, 4, 5, 6]
target = 6
index = Solution.twoSum(nums, target)
try:
    print("Los indices son: ", index)
    print("corresponde a los numeros: ", nums[index[0]], nums[index[1]])
except:
     print("No se encontró una solucion.")
