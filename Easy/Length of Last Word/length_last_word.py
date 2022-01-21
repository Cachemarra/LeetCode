#%% Clase solucion
class Solution:
    # First Solution.
    '''
    def lengthOfLastWord(self, s: str) -> int:
        # Create a list of words
        list_of_words = s.split(' ')

        # Clean all spaces
        clean_list = [x for x in list_of_words if x]

        print(f'list_of_words: {clean_list}')
        return len(clean_list[-1])
    '''
    # Second Solution. Shortest.
    def lengthOfLastWord(self, s: str) -> int:
        # Create a list of words
        return len(s.split()[-1])


#%% Pruebas
if __name__ == '__main__':

    test_cases = ["Hello World", "   fly me   to   the moon  ", "luffy is still joyboy"]
    results = [5, 4, 6]
    count = 0

    for index, item in enumerate(test_cases):
        ans = Solution().lengthOfLastWord(item)
        print(f'We get: {ans}, expected: {results[index]}')
        if ans == results[index]:
            print('Passed')
            count += 1
        else:
            print('Failed')
        print('\n')

    print(f'We passed {count} out of {len(test_cases)} test cases')

# %%
