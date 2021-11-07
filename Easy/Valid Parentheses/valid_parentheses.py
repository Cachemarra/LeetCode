'''
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        # Variable to flag if there's a valid stack
        valid = False
        # If length of the string is 0, return True
        if len(s) == 0:
            return True

        # Define a stack to store the opening parentheses
        stack = []

        # Main for to iterate through the string
        for i in s:
            # Look if the first character is an opening parentheses
            if i == '(' or i == '[' or i == '{':
                # If so, push it to the stack
                stack.append(i)
                valid = True

            # Look if the stack has a value
            elif len(stack) == 0:
                return False
            # Look if the first character is a closing parentheses
            elif i == ')' and stack[-1] == '(' and valid:
                # If so, pop the last element from the stack
                stack.pop()

            elif i == ']' and stack[-1] == '[' and valid:
                stack.pop()

            elif i == '}' and stack[-1] == '{' and valid:
                stack.pop()
            # Only parentheses are expected. If the char is not, return False
            else:
                return False
        if len(stack) == 0:
            return True
        # If there's still elements in the stack, return False
        else:
            return False

                
if __name__ == '__main__':
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid(""))
    print(s.isValid("]"))


