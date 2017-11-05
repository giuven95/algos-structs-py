class LLNode:
    def __init__(self, data, aft):
        self.data = data
        self.aft = aft

    def insert_after(self, data):
        self.aft = LLNode(data, self.aft)

    def remove_after(self):
        self.aft = self.aft.aft


class LinkedList:
    def __init__(self, data):
        self.head = LLNode(data, None)

    def traverse(self, func):
        cursor = self.head
        while cursor:
            func(cursor.data)
            cursor = cursor.aft

    def insert_head(self, data):
        self.head = LLNode(data, self.head)

    def insert_tail(self, data):
        tail = self.get_tail()
        tail.insert_after(data)

    def remove_head(self):
        self.head = self.head.aft  # older head is garbage collected

    def get_tail(self):
        if self.head is None:
            return None
        cursor = self.head
        while cursor.aft:  # !!!
            cursor = cursor.aft
        return cursor

    def append(self, ll2):
        tail = self.get_tail()
        tail.aft = ll2.head


if __name__ == "__main__":
    ll = LinkedList(10)
    ll2 = LinkedList("a")
    ll.append(ll2)
    ll.traverse(print)  # 10 a
    print("##########")
    ll.insert_tail("b")
    ll.insert_tail("b")
    ll.insert_tail(7.77)
    ll.insert_head(11)
    ll.traverse(print)  # 11 10 a b b 7.77
    print("##########")
    for i in range(4):
        ll.remove_head()
    ll.traverse(print)  # b 7.77

    # unsafe -> ll.append(ll) causes infinite recursion
