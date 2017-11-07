class DLLNode:
    def __init__(self, data, prev, link):
        self.data = data
        self.prev = prev
        self.link = link


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def traverse(self, func):
        cursor = self.head
        while cursor:
            func(cursor.data)
            cursor = cursor.link

    def prepend(self, data):
        if self.is_empty():
            self.head = DLLNode(data, None, None)
            self.tail = self.head
            self.length += 1
        else:
            self.insert_before(self.head, data)

    def append(self, data):
        if self.is_empty():
            self.prepend(data)
        else:
            self.insert_after(self.tail, data)

    def get_at(self, index):
        if index < 0:
            index = self.length + index

        if self.is_empty() or not (0 <= index < self.length):
            return None

        if index <= self.length // 2:
            i = 0
            cursor = self.head
            while cursor and i < index:
                cursor = cursor.link
                i += 1
        else:
            i = self.length - 1
            cursor = self.tail
            while cursor and i > index:
                cursor = cursor.prev
                i -= 1
        return cursor

    def insert_before(self, node, data):
        node.prev = DLLNode(data, node.prev, node)
        self.__connect(node.prev.prev, node.prev)
        self.length += 1

    def insert_after(self, node, data):
        node.link = DLLNode(data, node, node.link)
        self.__connect(node.link, node.link.link)
        self.length += 1

    def remove_before(self, node):
        if node.prev:
            self.__connect(node.prev.prev, node)
            self.length -= 1
        else:
            raise IndexError("Nothing to remove!")

    def remove_after(self, node):
        if node.link:
            self.__connect(node, node.link.link)
            self.length -= 1
        else:
            raise IndexError("Nothing to remove!")

    def concatenate(self, ll2):
        ll2 = ll2.copy()
        self.__connect(self.tail, ll2.head)
        self.tail = ll2.tail

        self.length += ll2.length

    def copy(self):
        ll = DoublyLinkedList()
        self.traverse(lambda data: ll.append(data))
        return ll

    def print_data(self):
        self.traverse(print)

    def __connect(self, node1, node2):
        if node1:
            node1.link = node2
        if node2:
            node2.prev = node1
        for node in (node1, node2):
            self.__update(node)

    def __update(self, node):
        if node is None:
            return
        if node.link is None:
            self.tail = node
        if node.prev is None:
            self.head = node


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll2 = DoublyLinkedList()
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
        ll.remove_before(ll.get_at(1))
    ll.print_data()  # b 7.77
    print("##########")

    ll.concatenate(ll)
    ll.concatenate(ll)
    ll.prepend("samba")
    ll.print_data()  # samba b 7.77 b 7.77 b 7.77 b 7.77
    print("##########")

    node = ll.get_at(3)
    for i in range(3):
        ll.remove_before(node)
    ll.insert_before(node, "AAA")
    ll.insert_after(node, "CCC")
    ll.print_data()  # AAA b CCC 7.77 b 7.77 b 7.77
