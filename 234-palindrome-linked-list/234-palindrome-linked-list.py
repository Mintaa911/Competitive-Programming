# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal_list = []
        
        while head:
            pal_list.append(head.val)
            head = head.next
            
        return pal_list == pal_list[::-1]