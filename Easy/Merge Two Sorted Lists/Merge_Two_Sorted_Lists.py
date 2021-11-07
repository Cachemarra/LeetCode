'''
# Merge two sorted linked lists and return it as a sorter list.
# The list should be made by splicing together the nodes of the first two lists.

# Constraints:
# * The number of nodes in both lists is in the range [0, 50]
# * -100 <= Node.val <= 100
# * Both l1 and l2 are sorted in non-decreasing order.


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, val=0, next=None):
#       self.val = val
#       self.next = next

'''

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # If there's not a list, it return the other list
        if not l1:
            return l2
        if not l2:
            return l1

        # Sorting
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

        

