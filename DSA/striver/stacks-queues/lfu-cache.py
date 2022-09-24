from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1


class DLinkedList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0

    def append(self, node) -> None:
        next = self.head.next
        node.prev, node.next = self.head, next
        next.prev = node
        self.head.next = node
        self.size += 1

    def pop(self, node=None) -> Optional[Node]:
        if self.size == 0:
            return None
        if not node:
            node = self.tail.prev
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        self.size -= 1
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.pageMap = dict()
        self.freqMap = defaultdict(DLinkedList)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.pageMap:
            return -1
        node = self.pageMap[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.pageMap:
            node = self.pageMap[key]
            self.update(node)
            node.val = value
        else:
            if self.size == self.capacity:
                nodeToRemove = self.freqMap[self.minFreq].pop()
                del self.pageMap[nodeToRemove.key]
                self.size -= 1
            node = Node(key, value)
            self.pageMap[key] = node
            self.size += 1
            self.freqMap[1].append(node)
            self.minFreq = 1

    def update(self, node: Node) -> None:
        nodeFreq = node.freq
        self.freqMap[nodeFreq].pop(node)

        if nodeFreq == self.minFreq and self.freqMap[nodeFreq].size == 0:
            self.minFreq += 1

        newFreq = nodeFreq + 1
        node.freq = newFreq
        self.freqMap[newFreq].append(node)
