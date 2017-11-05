from numpy import empty

MAX_SIZE = 5000  # arbitrary constant

class Stack:
    def __init__(self, max_size=MAX_SIZE):
        # array of integers
        self.data = empty(max_size, dtype=int)
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0
        
    def is_full(self):
        return self.size == self.max_size

    def push(self, p):
        if self.is_full():
            raise Exception("Stack is already full!")
        else:
            self.data[self.size] = p
            self.size += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is already empty!")
        else:
            p = self.data[self.size - 1]
            self.size -= 1
            return p
