"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result
be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter whaty you leave beyond the
first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place
with O(1) extra memory.

Custom Judge:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.


Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1, 2, _]
Explanation: Your function should return k=2, with the first two elements of nums being
1 and 2 respectively. It doesn't matter what you leave beyond the returned k (hence
they are underscores).


Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
Explanation: Your function should return k = 5, with the first five elements of nuyms being
0, 1, 2, 3 and 4 respectively. It doesn't matter what you leave beyond the returned k (hence
they are underscores).

"""

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        # Variable to store the current integer. I use a large negative number
        current_numer = -1_000
        unique = 0
        # Check if the list is empty
        length = len(nums)
        if length == 0:
            return []

        # Iterate through the list and check if the element is unique    
        for i, item in enumerate(nums.copy()):
            # If there's a '_', then break the loop
            if item == '_':
                break
            # Store the integer only if is bigger than actual number
            elif current_numer < item:
                current_numer = item
                unique += 1
            
            # If the current element is the same as the last iteration, we can
            # suppose that we have an repeated number
            else:
                nums.pop(unique)
                nums.append('_')

        return nums


"""
            else:
                nums.remove(item)#            
"""

if __name__ == '__main__':
    # nums = [1, 1, 2, 2, 3, 3, 5, 6, 7, 7]
    # nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1, 1, 2]
    print(nums)
    print(Solution().removeDuplicates(nums))


