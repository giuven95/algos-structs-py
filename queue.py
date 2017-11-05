from numpy import empty

MAX_SIZE = 5000

class Queue:
    def __init__(self, max_size=MAX_SIZE):
        self.data = empty(max_size, dtype=int)
        self.head = 0
        self.tail = 0
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0
        
    def is_full(self):
        return self.size == self.max_size

    def put(self, p):
        if self.is_full():
            raise Exception("Queue is already full!")
        else:
            self.data[self.tail] = p
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def get(self):
        if self.is_empty():
            raise Exception("Queue is already empty!")
        else:
            p = self.data[self.head]
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return p
