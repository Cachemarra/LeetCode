# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 19:43:06 2020

@author: luisx

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        i = True
        dec = x
        inv = 0
        neg = False
        if 0 > x:
            neg = True
            dec *= -1

        while i:
            inv *= 10
            res = dec % 10
            dec = (dec - res) / 10
            inv += res
            if 0 == dec:
                i = False
                break

        if neg:
            inv *= -1
        if -2 ** 31 > inv or 2 ** 31 < inv:
            return 0
        return int(inv)
    
"""
Respuesta pro
class Solution:
    def reverse(self, x: int) -> int:
        rev = int(str(abs(x))[::-1])
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0

"""
# %% Main program


nums = -123
res = Solution().reverse(nums)
print("El resultado es: ", res)
