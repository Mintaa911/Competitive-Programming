class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        
        for i in range(len(lists)):
            head = lists[i]         
            while head:
                heapq.heappush(heap,head.val)
                head = head.next
        
        if not heap:
            return None
        head = ListNode(heapq.heappop(heap))
        cur_node = head
        
        while heap:
            new_node = ListNode(heapq.heappop(heap))
            cur_node.next = new_node
            cur_node = new_node
            
        return head
