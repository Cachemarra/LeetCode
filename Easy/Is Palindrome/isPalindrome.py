# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:42:53 2020

@author: luisx

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""
"""
# Version 1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        i = True
        dec = x
        inv = 0
        if 0 > x:
            return False

        while i:
            inv *= 10
            res = dec % 10
            dec = (dec - res) / 10
            inv += res
            if 0 == dec:
                i = False
                break
        if inv == x:
            return True
        else:
            return False
"""

"""
# Version 2

class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        dec = x
        inv = 0
        if 0 > x or (x % 10 == 0 and x != 0):
            return False

        while x > inv:
            inv *= 10
            res = dec % 10
            dec = (dec - res) / 10
            inv += res
            if inv == dec:
                return True
        return x == inv or x == inv / 10
"""

"""
# version de algun pro


"""

# %% Main program

num = 1220

palindromo= Solution().isPalindrome(num)

print("La respuesta es:", palindromo)
