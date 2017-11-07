from linked_list import LLNode
'''
This version of LinkedList boasts faster insertion at the end of the
list.
'''


class TailedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def traverse(self, func):
        cursor = self.head
        while cursor:
            func(cursor.data)
            cursor = cursor.link

    def prepend(self, data):
        self.head = LLNode(data, self.head)
        if self.head.link is None:
            self.tail = self.head

    def append(self, data):
        if self.is_empty():
            self.prepend(data)
        else:
            self.insert_after(self.tail, data)

    def remove_head(self):
        self.head = self.head.link
        if self.head is None:
            self.tail = None

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
        if node.link.link is None:
            self.tail = node.link

    def remove_after(self, node):
        if node.link:
            node.link = node.link.link
            if node.link is None:
                self.tail = node
        else:
            raise IndexError("Nothing to remove!")

    def concatenate(self, ll2):
        ll2 = ll2.copy()
        self.tail.link = ll2.head
        self.tail = ll2.tail

    def copy(self):
        ll = TailedList()
        self.traverse(lambda data: ll.append(data))
        return ll

    def print_data(self):
        self.traverse(print)


if __name__ == "__main__":
    ll = TailedList()
    ll2 = TailedList()
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
