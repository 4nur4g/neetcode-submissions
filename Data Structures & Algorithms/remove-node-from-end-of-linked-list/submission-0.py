# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        current = dummy
        # initial phase
        pointer1 = dummy
        pointer2 = dummy
        i = 0
        while i < n:
            pointer2 = pointer2.next
            i += 1
        while pointer2.next != None:
            pointer2 = pointer2.next
            current = current.next
        current.next = current.next.next

        return dummy.next

        