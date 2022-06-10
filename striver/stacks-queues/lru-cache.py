from collections import OrderedDict

class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    # Using OrderedDict
    # def __init__(self, capacity: int):
    #     self.capacity = capacity
    #     self.cache = OrderedDict()

    # def get(self, key: int) -> int:
    #     if key not in self.cache: return -1
    #     self.cache.move_to_end(key)
    #     return self.cache[key]

    # def put(self, key: int, value: int) -> None:
    #     if key in self.cache: del self.cache[key]
    #     self.cache[key] = value
    #     if len(self.cache) > self.capacity:
    #         self.cache.popitem(last=False)

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.hm: return -1
        node = self.hm[key]
        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self._remove(self.hm[key])
        node = Node(key, value)
        self._add(node)
        self.hm[key] = node
        if len(self.hm) > self.capacity:
            removeNode = self.tail.prev
            self._remove(removeNode)
            del self.hm[removeNode.key]
    
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next, next.prev = next, prev

    def _add(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)