# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    @staticmethod
    def get_ind(i, n):
        if i % 2 == 0:
            return i // 2
        else:
            return n - 1 - (i//2)

    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        temp = []
        for i in range(0, len(nodes)):
            temp.append(nodes[self.get_ind(i, len(nodes))])
        
        # dummy = ListNode() 
        # curr = dummy
        curr = head

        for i in range(1, len(temp)):
            curr.next = temp[i]
            curr = curr.next
        curr.next = None
        
        


        

        