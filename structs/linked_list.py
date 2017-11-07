'''
This is a minimal implementation.
LinkedList.append() is currently an operation of O(n) time complexity;
the operation can be made to have O(1) time complexity by adding
an attribute "self.tail" to the LinkedList class
'''


class LLNode:
    def __init__(self, data, link):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def traverse(self, func):
        cursor = self.head
        while cursor:
            func(cursor.data)
            cursor = cursor.link

    def prepend(self, data):
        self.head = LLNode(data, self.head)

    def append(self, data):
        if self.is_empty():
            self.prepend(data)
        else:
            tail = self.get_tail()
            self.insert_after(tail, data)

    def remove_head(self):
        self.head = self.head.link  # older head is garbage collected

    def get_tail(self):
        cursor = self.head
        while cursor.link:
            cursor = cursor.link
        return cursor

    def get_at(self, index):
        if self.is_empty() or index < 0:
            return None

        i = 0
        cursor = self.head
        while cursor and i < index:
            cursor = cursor.link
            i += 1
        return cursor

    def insert_after(self, node, data):
        node.link = LLNode(data, node.link)

    def remove_after(self, node):
        if node.link:
            node.link = node.link.link
        else:
            raise IndexError("Nothing to remove!")

    def concatenate(self, ll2):
        ll2 = ll2.copy()
        tail = self.get_tail()
        tail.link = ll2.head

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
