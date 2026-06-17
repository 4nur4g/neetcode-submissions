# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right_half = slow.next

        slow.next = None

        left_half = head

        curr = right_half
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        inverted_right_half = prev

        a = left_half
        b = inverted_right_half

        while a and b:
            a_next = a.next
            b_next = b.next

            a.next = b
            
            if not a_next:
                break

            b.next = a_next

            a = a_next
            b = b_next

        
