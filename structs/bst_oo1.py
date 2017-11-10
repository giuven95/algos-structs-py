class BinarySearchTree:
    def __init__(self, keys, values):
        self.root = BSTNode(keys[0], values[0])
        for (key, value) in zip(keys[1:], values[1:]):
            self.put(key, value)
            
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.search(key)

    def put(self, key, value):
        if self.root is None:
            self.root = BSTNode(key, value)
        else:
            self.root.insert(key, value)

    # in - order - traversal
    def iotraverse(self, func):
        if self.root is None:
            raise Exception("Empty tree")
        else:
            self.root.iotraverse(func)

    def delete(self, key):
        if self.root is None:
            raise Exception("Empty tree")
        elif key != self.root.key:
            self.root.delete(key)
        elif not (self.root.left or self.root.right):
            # root exists but has no children?
            self.root = None
        else:
            self.root._delete()


class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def search(self, key):
        if key == self.key:
            return True
        elif key < self.key and self.left:
            return self.left.search(key)
        elif key > self.key and self.right:
            return self.right.search(key)
        else:
            return None

    def insert(self, key, value):
        if key == self.key:
            # the key is already present in the tree
            self.value = value
        elif key < self.key:
            if self.left is None:
                self.left = BSTNode(key, value)
            else:
                self.left.insert(key, value)
        elif key > self.key:
            if self.right is None:
                self.right = BSTNode(key, value)
            else:
                self.right.insert(key, value)

    def iotraverse(self, func):
        if self.left:
            self.left.iotraverse(func)
        func(self.value)
        if self.right:
            self.right.iotraverse(func)

    def delete(self, key):
        if key < self.key and self.left is not None:
            if key == self.left.key:
                self.left._delete()
            else:
                self.left.delete(key)
        elif key > self.key and self.right is not None:
            if key == self.right.key:
                self.right._delete()
            else:
                self.right.delete(key)
        elif key != self.key:
            raise KeyError
        else:
            raise Exception("root cannot be deleted")

    def _delete(self):
        if self.right:
            self.key = self.right.key
            self.value = self.right.value
            self.right = self.right.right

        elif self.left:
            self.key = self.left.key
            self.value = self.left.value
            self.left = self.left.left

        else:  # node to delete has two children
            cursor = self.right
            parent = None

            while cursor.left:
                parent = cursor
                cursor = cursor.left

            self.key = cursor.key
            self.value = cursor.value
            if parent is not None:
                parent.left._delete()
            else:
                self.right._delete()


'''       
    def __repr__(self):
        s = "\nnode" + repr(self.key)
        if self.left is not None:
            s = s + "\nlk " + repr(self.left.key)
        if self.right is not None:
            s = s + "\nrk " + repr(self.right.key)
        return s
'''
if __name__ == "__main__":
    l = [100, 100, 100, 100, 100, 0, 1, 2, 5, 6, 4, 3, 3, 77, 45, 66, 23,
         22, 33, 100, 77, 5, 4, 26, 15, 13, 55, 57, 29, 21, 0, 0, 36, 22,
         19, 18, 15, 14, 81, 83, 85, 87, 89]
    bst = BinarySearchTree(l, l)
    bst.iotraverse(print)
    print("####################################")
    bst.delete(4)
    bst.delete(55)
    bst.delete(0)
    bst.delete(77)
    bst.iotraverse(print)
