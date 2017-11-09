from numpy import empty
from binary_heap import BinaryHeap


class PriorityQueue:
    def __init__(self, capacity=1000, heap_class=BinaryHeap):
        self.heap = heap_class(capacity)
        self.capacity = capacity

    def is_empty(self):
        return self.heap.size == 0

    def is_full(self):
        return self.heap.size == self.capacity

    def put(self, p, priority=0):
        if self.is_full():
            raise Exception("Queue is already full!")
        self.heap.insert(key=priority, value=p)

    def get(self):
        p = self.peek()
        self.heap.delete_root()
        return p

    # return obj with the highest priority without popping it out
    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        return self.heap.get_root()
