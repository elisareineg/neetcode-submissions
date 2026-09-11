# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    merged.append(self.mergeTwoLists(lists[i], lists[i+1]))
                else:
                    merged.append(lists[i])
            lists = merged
        return lists[0] # head of list

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        while list1:
            tail.next = list1
            list1 = list1.next
            tail = tail.next
        while list2:
            tail.next = list2
            list2 = list2.next
            tail = tail.next
        return dummy.next
                
        

        


        