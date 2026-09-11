# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Method 1: Recursion
        dummy = ListNode() # create instance of list
        tail = dummy

        while l1 and l2: # while they are not null
            if l1.val < l2.val: # if node at l1 is less than node at l2
                tail.next = l1 # update next node
                l1 = l1.next # update next pointer for l1
            else: # if node at l2 is less than or equal to node at l1
                tail.next = l2
                l2 = l2.next
            tail = tail.next # update this pointer outside of conditionals regardless for each pass
        
        # need another if condition in case we reach end of one of the linked lists
        # and the next pointer is null . These only execute once one of the lists is null
        if l1: 
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next # the whole linked list
