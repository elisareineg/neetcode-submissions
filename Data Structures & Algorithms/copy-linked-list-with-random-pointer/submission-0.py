"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        address = {None: None}


        # create copies of all nodes in one iteration, store original node -> copy

        first = head
        while first:
            tmpVal, nxt, tmpRandom = first.val, first.next, first.random
            copy = Node(tmpVal, nxt, tmpRandom)
            address[first] = copy
            first = first.next

        second = head
        while second:
            copy = address[second]
            copy.next = address[second.next]
            copy.random = address[second.random]
            second = second.next

        return address[head]