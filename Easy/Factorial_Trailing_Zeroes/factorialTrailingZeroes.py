"""
Factorial Trailing Zeroes

@author: Luis Xavier Nevarez

This function returns the number of trailing zeroes in n!

"""
#%% Class definition
class Solution:
    def trailingZeroes(self, n: int) -> int:
        # Variables
        modulus = 0 # for remainder of modulus operation
        zeroes = 0 # Store the number of zeros of n!
        # In case there's no n or isn't passed, return 0
        if not n:
            return 0
        # otherwise:
        else:
            # Get the factorial of n
            n = self.factorial(n)

            # If n < 10 there's no trailing 0.
            if n < 10:
                return 0
            # Otherwise
            else:
                # TODO trailing zeroes are CONSECUTIVE zeroes at the end.
                while(n != 0):
                    # get the remainder
                    modulus = n % 10

                    # If modulus == 0 we found a 0.
                    if modulus == 0:
                        zeroes += 1
                    # Otherwise
                    else:
                        return zeroes
                    # reduce a decimal.
                    n = n // 10
                
                # Once the loop has finished, we have our answer
                return zeroes
        

    # A factorial method used by trailingZeroes
    def factorial(self, n: int) -> int:
        if n == 0:
            return 1
        # Recursive function.
        else:
            n *= self.factorial(n-1)
            return n


#%% Test of class
if __name__ == '__main__':

    # Test inputs
    n = [7, 3, 5, 0, 10, 4, 12, 30]

    # Create a Solution object
    solution = Solution()

    for item in n:
        print(item, ' <- number')
        print(solution.factorial(item), ' <- Factorial')
        print(solution.trailingZeroes(item), ' <- zeroes')
        print('=================')

