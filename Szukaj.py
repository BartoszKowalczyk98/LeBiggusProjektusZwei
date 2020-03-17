import random
import matplotlib.pyplot as plt
from Stan import Stan
from Potomstwo import potomstwo

howManyCities = int(input("Podaj liczbe miast: "))
cities = []
for i in range(howManyCities):
    cities.insert(i, [i, random.randint(1, 40), random.randint(1, 40)])

currentState = Stan()
i = random.randrange(0, howManyCities)
currentState.setCurrentCity(i)
currentState.addPath(i)

states = potomstwo(currentState, cities)

while len(states[0].path)!=howManyCities:
    appender = []
    for i in states:
        temp = potomstwo(i,cities)
        for j in temp:
            appender.append(j)
    states = appender







print("miasto z którego startujemy: " + i.__str__())
for i in range(len(states)):
    print(states[i].path)

x = []
y = []
for i in range(howManyCities):
    x.append(cities[i][1])
    y.append(cities[i][2])
plt.scatter(x, y)
plt.show()
