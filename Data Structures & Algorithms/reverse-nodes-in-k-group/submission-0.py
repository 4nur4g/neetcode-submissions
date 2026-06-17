# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseLinkedList(self,head, k):
        curr = head
        prev = None
        counter = 0
        while curr and counter < k:
            
            temp = curr.next
            curr.next = prev

            prev = curr
            curr = temp
            counter += 1
        # prev is new head, current is next group start
        return prev, curr


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        last_group_end = dummy

        while True:
            group_start = last_group_end.next
            curr = group_start
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            if count < k:
                break

            new_head, next_group_start = self.reverseLinkedList(group_start, k)

            last_group_end.next = new_head

            group_start.next = next_group_start

            last_group_end = group_start
        return dummy.next
        