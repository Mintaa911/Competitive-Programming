# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l_headA,l_headB = 0,0
        curA,curB = headA,headB
        
        while curA:
            curA = curA.next
            l_headA += 1
            
        while curB:
            curB = curB.next
            l_headB += 1
            
        d = abs(l_headA-l_headB)
        curA,curB = headA,headB
        
        if l_headA > l_headB:
            for i in range(d):
                curA = curA.next
        else:
            for i in range(d):
                curB = curB.next
                
        while curA and curB:
            if curA == curB:
                return curA
            
            curA = curA.next
            curB = curB.next
            
        return None
        
        
        