# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        len_head = 0
        dummy = head

        while dummy:
            len_head += 1
            dummy = dummy.next
        
        if len_head == n:
            return head.next

        diff = len_head - n
        cur = 0
        dummy = head

        while dummy:
            cur += 1

            if cur == diff:
                dummy.next = dummy.next.next

            dummy = dummy.next
            
        return head