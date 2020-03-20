from filecmp import cmp


class Stan:
    currentCity = -1
    path = []
    cost = 0

    def __lt__(self, other):
        return self.cost < other.cost