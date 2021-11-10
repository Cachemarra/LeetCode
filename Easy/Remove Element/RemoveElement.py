"""
Given an integer array nums and an integer val, remove all occurrences of val
in nums in-place. The relative order of the elements may be changed.

Since it is impossible to change the length of the array  in some languagees, 
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates, then the first 
k elements of nums should hold the final result. It does not matter what you leave 
beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by
modifying the input array in-place with O(1) extra memory.

Custom Judge:
The judge will test your solution with the following code:

int [] nums = [...]; // Input Array
int val = ...; // Value to remove
int [] expectedNums = [...]; // The expected answer with the correct length
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}

If all assertions pass, then your solution will be accepted.

Example 1:

Inputs: nums = [3, 2, 2, 3], val = 3
Output: 2, nums = [2, 2, _, _]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Inputs: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: 5, nums = [0, 1, 4, 0, 3, _, _, _]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 1, 4, 0, and 3.
Note that the five elements can be returned in any order.
It doesn't matter what values are set beyond the returned k (hence they are underscores).

Constraints:
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""

class Solution:

    def removeElement(self, full_list: list(), delete_number: int) -> int:
        # variable to store the size of the list
        list_len = len(full_list)
        value_key = 0
        # If an empty list is passed it return a 0
        if not full_list:
            return 0

        # Else
        else:
            # Main loop to iterate through the list
            for i in range(len(full_list)):

                # Check if the list number is the same as the number to delete
                if full_list[value_key] == delete_number:
                    # If so, it pop it and append a '_'.
                    full_list.pop(value_key)
                    full_list.append('_')
                    list_len -= 1
                else:
                    # If not, the index increment by 1.
                    value_key += 1

            return list_len



# Funcionamiento standard.
if __name__ == '__main__':
    
    # Listas de prubeas
    nums = [3, 2, 2, 3]
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    
    # Creamos el objeto y llamamos a su metodo
    solucion = Solution()
    ans_list, ans_size = solucion.removeElement(nums, 2)


    print('Resultado: ')
    print(f'List: {ans_list}, with size: {ans_size}')
