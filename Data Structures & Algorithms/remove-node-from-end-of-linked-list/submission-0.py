# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        first, second = head, dummy

        for i in range(n):
            first = first.next
        while first:
            first = first.next
            second = second.next # should be second last at end

        # second.next: nth node to end
        idx = second.next 
        nxt = idx.next
        second.next = nxt


        return dummy.next


        


        