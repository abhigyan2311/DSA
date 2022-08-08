from collections import defaultdict

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.freq = 1
        self.next = self.prev = None

class DLinkedList:
    def __init__(self) -> None:
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head
        self._size = 0
    
    def append(self, node) -> None:
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node
        self._size += 1

    def pop(self, node=None) -> None:
        if self._size == 0: return
        if not node: 
            node = self.tail.prev
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev
        self._size -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        self._hm = dict()
        self._fm = defaultdict(DLinkedList)
        self._minFreq = 0

    def update(self, node) -> None:
        """ 
        This is a helper function that used in the following two cases:
        
            1. when `get(key)` is called; and
            2. when `put(key, value)` is called and the key exists.
         
        The common point of these two cases is that:
        
            1. no new node comes in, and
            2. the node is visited one more times -> node.freq changed -> 
               thus the place of this node will change
        
        The logic of this function is:
        
            1. pop the node from the old DLinkedList (with freq `f`)
            2. append the node to new DLinkedList (with freq `f+1`)
            3. if old DlinkedList has size 0 and self._minFreq is `f`,
               update self._minFreq to `f+1`
        
        All of the above opeartions took O(1) time.
        """

        freq = node.freq

        # Pop the node from old DLinkedList with freq f
        self._fm[freq].pop(node)

        if self._minFreq == freq and self._fm[freq]._size == 0:
            self._minFreq += 1
        
        node.freq += 1
        freq = node.freq
        self._fm[freq].append(node)

    def get(self, key: int) -> int:
        if key not in self._hm: return -1
        node = self._hm[key]
        self.update(node)
        return node.val      


    def put(self, key: int, value: int) -> None:
        if self._capacity == 0: return

        if key in self._hm:
            node = self._hm[key]
            self.update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._fm[self._minFreq].pop()
                del self._hm[node.key]
                self._size -= 1
            
            node = Node(key, value)
            self._hm[key] = node
            self._fm[1].append(node)
            self._minFreq = 1
            self._size += 1



# Your LFUCache object will be instantiated and called as such:
obj = LFUCache(2)
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
print(obj.get(3))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))

1-2
3-2