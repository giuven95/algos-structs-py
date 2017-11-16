class Tower:
    def __init__(self, name, disks=None):
        self.name = name
        if disks is None:
            disks = []
        self.disks = disks

    def move_one(self, dest):
        if len(dest.disks) == 0 or self.disks[-1] < dest.disks[-1]:
            disk = self.disks[-1]
            self.disks = self.disks[:-1]
            dest.disks.append(disk)
        else:
            raise Exception("Must stack disk above bigger disk")

    def move_many(self, aux, dest, num):
        if num == 1:
            self.move_one(dest)
        else:
            self.move_many(dest, aux, num - 1)
            self.move_one(dest)
            aux.move_many(self, dest, num - 1)

    def move_all(self, aux, dest):
        self.move_many(aux, dest, len(self.disks))

    def __repr__(self):
        s = "({}, {})".format(self.name, self.disks)
        return s


class Game:
    def __init__(self, num_disks):
        disks = list(range(num_disks, 0, -1))
        a = Tower("A", disks)
        b = Tower("B")
        c = Tower("C")
        self.towers = (a, b, c)

    def run(self):
        (a, b, c) = self.towers
        a.move_all(b, c)

    def display(self):
        print("\n")
        for t in self.towers:
            print(t)


if __name__ == "__main__":
    game = Game(5)
    game.display()

    game.run()
    game.display()
