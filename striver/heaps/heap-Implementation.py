class MinHeap:
    def __init__(self, capacity) -> None:
        self.storage = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
       return (index-1)//2
    def getLeftChildIndex(self, index):
        return (2*index) + 1
    def getRightChildIndex(self, index):
        return (2*index) + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity
        
    def swap(self, index1, index2):
        self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]
    
    # Iteration
    def insert(self, data):
        if self.isFull(): raise Exception("Heap is full")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()
    
    def heapifyUp(self):
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) > self.storage[index]):
            parentIndex = self.getParentIndex(index)
            self.swap(index, parentIndex)
            index = parentIndex
    
    # Iteration
    def removeMin(self):
        if self.size == 0: raise Exception("Heap is empty!")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size-1]
        self.storage[self.size - 1] = None
        self.size -= 1
        self.heapifyDown()
        return data


    def heapifyDown(self):
        index = 0
        while(self.hasLeftChild(index)):
            smallestChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index):
                smallestChildIndex = self.getRightChildIndex(index)
            if self.storage[index] < self.storage[smallestChildIndex]: break
            self.swap(index, smallestChildIndex)
            index = smallestChildIndex
    
    # Recursive
    # def insert(self, data):
    #     if self.isFull(): raise Exception("Heap is full")
    #     self.storage[self.size] = data
    #     self.size += 1
    #     self.heapifyUp(self.size - 1)
    
    # def heapifyUp(self, index):
    #     if (self.hasParent(index) and self.parent(index) > self.storage[index]):
    #         self.swap(self.getParentIndex(index), index)
    #         self.heapifyUp(self.getParentIndex(index))

    # def removeMin(self):
    #     if self.size == 0: raise Exception("Empty Heap")
    #     data = self.storage[0]
    #     self.storage[0] = self.storage[self.size-1]
    #     self.size -= 1
    #     self.heapifyDown(0)
    #     return data
    
    # def heapifyDown(self, index):
    #     smallest = index
    #     if self.hasLeftChild(index) and self.storage[smallest] > self.getLeftChildIndex(index):
    #         smallest = self.getLeftChildIndex(index)
    #     if self.hasRightChild(index) and self.storage[smallest] > self.getRightChildIndex(index):
    #         smallest = self.getRightChildIndex(index)
    #     if smallest != index:
    #         self.swap(index, smallest)
    #         self.heapifyDown(smallest)

heap = MinHeap(7)
heap.insert(10)
heap.insert(20)
heap.insert(5)
heap.insert(8)
heap.insert(15)
heap.insert(30)
heap.insert(0)
print(heap.storage)
heap.removeMin()
print(heap.storage)
heap.removeMin()
print(heap.storage)