import random
import matplotlib.pyplot as plt
from Stan import Stan
from Potomstwo import potomstwo

howManyCities = int(input("Podaj liczbe miast: "))
cities = []
for i in range(howManyCities):
    cities.insert(i, [i, random.randint(1, 40), random.randint(1, 40)])

currentState = Stan()
index = random.randrange(0, howManyCities)
currentState.setCurrentCity(index)
currentState.addPath(index)

states = potomstwo(currentState, cities)

while len(states[0].path)!=howManyCities:
    appender = []
    for i in states:
        temp = potomstwo(i,cities)
        for j in temp:
            appender.append(j)
    states = appender


states.sort()
x = []
y = []
for i in states[0].path:
    x.append(cities[i][1])
    y.append(cities[i][2])

x.append(cities[states[0].path[0]][1])
y.append(cities[states[0].path[0]][2])
plt.plot(x, y)
for i in range(len(x)-1):
    label=states[0].path[i]+1
    plt.annotate(label,  # this is the text
                 (x[i], y[i]),  # this is the point to label
                 textcoords="offset points",  # how to position the text
                 xytext=(0, 10),  # distance from text to points (x,y)
                 ha='center')  # horizontal alignment can be left, right or center

plt.show()