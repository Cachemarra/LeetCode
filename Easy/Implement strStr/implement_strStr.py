'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle
is not part of the haystack.

## Clarification
What sould we return when needle is an empty string? This is great question
to ask during an interview.

For the purpose of this problem, we wil return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().


Example 1:
Input: haystack = 'hello', needle = 'll'
Output: 2

Example 2:
Input: haystack = 'aaaaaa', needle = 'bba'
Output: -1

Example 3:
Input: haystack = '', needle = ''
Output: 0


Constraints:
    * 0 <= haystack.length, needle.length <= 5 * 10^4
    * haystack and needle consist of only lower-case English characters.

'''


# Clase de la solución
class Solution:
    def strStr(self, haystrack: str, needle: str) -> int:
        # Length of needle
        needle_len = len(needle)

        # assert that there's a needle
        if not needle:
            return 0
        
        # Check if the needle is not in the haystrack
        if not (needle in haystrack):
            return -1

        # Main loop
        for i, item in enumerate(haystrack):
            # Check if the char is the same as first
            # in needle
            if item == needle[0]:
                # Check if all fits
                print(haystrack[i:i+needle_len])
                if haystrack[i:i+needle_len] == needle:
                    
                    return i


# Main code
if __name__ == '__main__':

    # variables de prubea
    haystrack = "hello"; needle = 'll'
    # haystrack = 'aaaaaa'; needle = 'bba'
    # haystrack = ''; needle = ''

    # Instanciamos el objeto y usamos el metodo
    solution = Solution()

    leng = solution.strStr(haystrack, needle)

    print(f'El indice es: {leng}, and words are: {[haystrack, needle]}')









