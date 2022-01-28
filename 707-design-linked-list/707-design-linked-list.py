class Node:
    def __init__(self,val=0,nxt=None):
        self.val = val
        self.next = nxt
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.counter = 0


    def get(self, index: int) -> int:
        if index < self.counter:
            cur_node = self.head
            for i in range(index):
                cur_node = cur_node.next
                
            return cur_node.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        self.counter += 1


    def addAtTail(self, val: int) -> None:
        cur_node = self.head
        if not self.head:
            self.addAtHead(val)
        else:
            for i in range(self.counter-1):
                cur_node = cur_node.next

            cur_node.next = Node(val)    
            self.counter += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif index == self.counter:
            self.addAtTail(val)
        elif index < self.counter:
            cur_node = self.head
            for i in range(index-1):
                cur_node = cur_node.next

            nxt_node = cur_node.next
            new_node = Node(val)
            cur_node.next = new_node
            new_node.next = nxt_node

            self.counter += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < self.counter:
            if index == 0:
                nxt_node = self.head.next
                self.head.next = None
                self.head = nxt_node
            else:
                cur_node = self.head
                for i in range(index-1):
                    cur_node = cur_node.next
                    
                remove_node = cur_node.next
                cur_node.next = remove_node.next
                remove_node.next = None
                
            self.counter -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)