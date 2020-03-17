class Stan:
    currentCity = -1
    path = []
    cost = 0

    def setCurrentCity(self, miasto):
        self.currentCity = miasto

    def addPath(self, miasto):
        self.path.append(miasto)

    def addCost(self, c):
        self.cost = self.cost + c
