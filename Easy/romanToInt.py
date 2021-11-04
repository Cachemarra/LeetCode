# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 16:58:03 2020

@author: luisx

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3

Example 2:

Input: "IV"
Output: 4

Example 3:

Input: "IX"
Output: 9

Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


# Solucion propia
class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
        ans = 0
        greek = list(s)
        i = 0
        while i < len(s):
            tam = len(greek)

            if greek == []:
                break
            elif greek[0] == 'I' and tam > 1 and (greek[1] == 'V' or
                                                  greek[1] == 'X'):
                ans += values[greek.pop(1)] - values[greek.pop(0)]
            elif greek[0] == 'X' and tam > 1 and (greek[1] == 'L' or
                                                  greek[1] == 'C'):
                ans += values[greek.pop(1)] - values[greek.pop(0)]
            elif greek[0] == 'C' and tam > 1 and (greek[1] == 'D' or
                                                  greek[1] == 'M'):
                ans += values[greek.pop(1)] - values[greek.pop(0)]
            else:
                ans += values[greek.pop(0)]
            i += 1
        return ans


"""
# Solucion pro
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':   1, 'V':   5, 'X':  10, 'L':  50,
               'C': 100, 'D': 500, 'M':1000           }
        integer = 0
        for i in range(len(s)-1):
            curr, later = dic[s[i]], dic[s[i+1]]
            if curr >= later:
                integer += curr
            else:
                integer -= curr
        integer += dic[s[-1]]
        return integer
"""
# %% Main program


numero = "LVIII"
ans = Solution().romanToInt(numero)
print(ans)
