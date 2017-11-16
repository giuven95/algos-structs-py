class HanoiTower:
    def __init__(self, name, ndisks):
        self.name = name
        self.ndisks = ndisks

    def move_one(self, dest):
        self.ndisks -= 1
        dest.ndisks += 1

    def move_many(self, help, dest, num):
        if num == 1:
            self.move_one(dest)
        else:
            self.move_many(dest, help, num - 1)
            self.move_one(dest)
            help.move_many(self, dest, num - 1)

    def move_all(self, help, dest):
        self.move_many(help, dest, self.ndisks)

    def __repr__(self):
        s = "({}, {})".format(self.name, self.ndisks)
        return s


if __name__ == "__main__":
    a = HanoiTower("A", 5)
    b = HanoiTower("B", 0)
    c = HanoiTower("C", 0)

    a.move_all(b, c)

    for tower in (a, b, c):
        print(tower)
