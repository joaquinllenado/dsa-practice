# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_length = 0
        dummy = head

        while dummy:
            list_length += 1
            dummy = dummy.next

        if list_length == n:
            return head.next
        
        diff = list_length - n
        cur = 0
        dummy = head

        while dummy:
            cur += 1
            if cur == diff:
                dummy.next = dummy.next.next
            dummy = dummy.next
        
        return head