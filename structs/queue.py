from numpy import empty


class Queue:
    def __init__(self, capacity=1000):
        self.data = empty(capacity, dtype=object)
        self.head = 0
        self.tail = 0
        self.size = 0
        self.capacity = capacity

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def put(self, p):
        if self.is_full():
            raise Exception("Queue is already full!")
        else:
            self.data[self.tail] = p
            self.tail = (self.tail + 1) % self.capacity
            self.size += 1

    def get(self):
        if self.is_empty():
            raise Exception("Queue is empty!")
        else:
            p = self.data[self.head]
            self.head = (self.head + 1) % self.capacity
            self.size -= 1
            return p
