# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:42:48 2020

@author: luisx

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.
"""


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res = ""
        # If nothing on string or just 1 element
        if len(strs) == 0:
            return res
        if len(strs) == 1:
            return strs[0]
        # Else
        SORT_WORDS = sorted(strs, key=len)
        MIN_WORD = len(SORT_WORDS[0])
        palabra = list(strs[0])
        equal = [True] * len(SORT_WORDS[-1])

        # First cicle. Start from next word and list it to "word"
        for i, word in enumerate(strs[1:]):
            word = list(word)
            mini = min(len(palabra), len(word))

            for j in range(mini):
                if not equal[j]:
                    break
                equal[j] = palabra[j] == word[j]
                # If is empty or has a False at 0 exit
            if equal == []:
                return res
            if not equal[0]:
                return res

        # check if all conditions are rquired
        for k, cond in enumerate(equal):
            if not cond:
                return res
            if k >= MIN_WORD:
                return res
            res += palabra[k]
        return res


# %% Main module

lista = ["baab", "bacb", "b", "cbc"]

sol = Solution().longestCommonPrefix(lista)

print(sol)
