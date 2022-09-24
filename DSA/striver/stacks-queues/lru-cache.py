class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pageMap = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.pageMap:
            return -1
        node = self.pageMap[key]
        # Remove node from DLL and add to beginning of the list
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.pageMap:
            self.remove(self.pageMap[key])
        node = Node(key, val)
        self.add(node)
        self.pageMap[key] = node
        if len(self.pageMap) > self.capacity:
            nodeToRemove = self.tail.prev
            self.remove(nodeToRemove)
            del self.pageMap[nodeToRemove.key]

    def remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def add(self, node: Node) -> None:
        next = self.head.next
        node.prev = self.head
        node.next = next
        self.head.next = node
        next.prev = node
