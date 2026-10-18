# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        # split list into two halves, reverse 2nd half and merge
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # unti last node

        secondHead = slow.next
        slow.next = None  # split
        prev, curr = None, secondHead
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # prev is now the head of the reversed second half

        # merge 
        while prev:
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            prev.next = tmp1
            head = tmp1
            prev = tmp2




        

            
        

        