'''
this is a minimal implementation
LinkedList.append() is currently an operation of O(n) time complexity
it can be made to have O(1) time complexity by adding
an attribute "self.tail" to the LinkedList class
'''


class LLNode:
    def __init__(self, data, aft):
        self.data = data
        self.aft = aft

    def insert_after(self, data):
        self.aft = LLNode(data, self.aft)

    def remove_after(self):
        self.aft = self.aft.aft


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def traverse(self, func):
        if self.is_empty():
            return None

        cursor = self.head
        while cursor.aft:
            func(cursor.data)
            cursor = cursor.aft

        func(cursor.data)
        return cursor

    def prepend(self, data):
        self.head = LLNode(data, self.head)

    def append(self, data):
        if self.is_empty():
            self.prepend(data)
        else:
            tail = self.get_tail()
            tail.insert_after(data)

    def remove_head(self):
        self.head = self.head.aft  # older head is garbage collected

    def get_at(self, index):
        i = 0
        cursor = self.head
        while cursor and i < index:
            cursor = cursor.aft
            i += 1
        return cursor
        
    def insert_at(self, index, data):
        if index <= 0:
            self.prepend(data)
        else:
            node = self.get_at(index - 1)
            node.insert_after(data)
        
    def get_tail(self):
        return self.traverse(lambda node: None)  # no - op lambda

    def concatenate(self, ll2):
        ll2 = ll2.copy()
        tail = self.get_tail()
        tail.aft = ll2.head

    def copy(self):
        ll = LinkedList()
        self.traverse(lambda data: ll.append(data))
        return ll

    def print_data(self):
        self.traverse(print)


if __name__ == "__main__":
    ll = LinkedList()
    ll2 = LinkedList()
    ll.append(10)
    ll2.append("a")
    ll.concatenate(ll2)
    ll.print_data()  # 10 a
    print("##########")

    ll.append("b")
    ll.append("b")
    ll.append(7.77)
    ll.prepend(11)
    ll.print_data()  # 11 10 a b b 7.77
    print("##########")

    for i in range(4):
        ll.remove_head()
    ll.print_data()  # b 7.77
    print("##########")

    ll.concatenate(ll)
    ll.concatenate(ll)
    ll.prepend("samba")
    ll.print_data()  # samba b 7.77 b 7.77 b 7.77 b 7.77
