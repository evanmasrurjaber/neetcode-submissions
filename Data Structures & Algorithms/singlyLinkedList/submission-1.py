class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next
        return -1
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.head
        for _ in range(index):
            if not prev.next:
                return False
            prev = prev.next
        if not prev.next:
            return False
        if prev.next == self.tail:
            self.tail = prev
        prev.next = prev.next.next
        return True

    def getValues(self) -> List[int]:
        curr = self.head.next
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        return arr
