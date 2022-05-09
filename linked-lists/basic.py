class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insertAtEnd(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
    
    def insertValues(self, lst):
        self.head = None
        for val in lst:
            self.insertAtEnd(val)

    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def removeAt(self, index):
        if index<0 or index>=self.getLength():
            raise Exception("Not a valid index")
        
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insertAt(self, index, data):
        if index<0 or index>=self.getLength():
            raise Exception("Not a valid index")
        
        node = Node(data, None)
        if index==0:
            node.next = self.head
            self.head = node
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node.next = itr.next
                itr.next = node
                break
            itr = itr.next
            count += 1
    
    def reverseList(self):
        prev = None
        current = self.head
        next = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        llstr = ""
        while itr:
            llstr = llstr + str(itr.data) + " --> "
            itr = itr.next
        print(llstr)

ll = LinkedList()
ll.print()
ll.insertValues([6,2,3,4,5])
ll.print()
print("Length of Linked List: ", ll.getLength())
ll.removeAt(2)
ll.insertAt(2, 1)
ll.insertAt(0, 7)
ll.print()
ll.reverseList()
ll.print()


