from swap import swap
from numpy import empty


class BHNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# implemented as an implicit data structure
class BinaryHeap:
    def __init__(self, capacity=1000):
        self.data = empty(capacity, dtype=BHNode)
        self.size = 0

    def get_root(self):
        return self.data[0].value

    def delete_root(self):
        swap(self.data, 0, self.size - 1)
        self.size -= 1

        self.__sift_down(0)

    def insert(self, key, value):
        self.data[self.size] = BHNode(key, value)
        self.size += 1

        index = self.size - 1
        self.__sift_up(index)

    def __sift_up(self, i):
        par = (i - 1) // 2
        while par >= 0 and self.data[i].key > self.data[par].key:
            swap(self.data, par, i)
            i = par
            par = (i - 1) // 2

    def __sift_down(self, i):
        cch = self.__choose_child(i)
        while cch < self.size and self.data[i].key < self.data[cch].key:
            swap(self.data, cch, i)
            i = cch
            cch = self.__choose_child(i)

    def __choose_child(self, i):
        ch1 = 2 * i + 1
        ch2 = 2 * i + 2
        if ch2 >= self.size or self.data[ch1].key > self.data[ch2].key:
            return ch1
        else:
            return ch2
