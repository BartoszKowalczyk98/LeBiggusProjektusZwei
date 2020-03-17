import copy
import math

from Stan import Stan


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def potomstwo(stan, miasta):
    howMany = len(miasta)


    if len(stan.path) >= howMany:
        print("Penis")
        return -1

    listaStanow = []

    for i in range(howMany):

        helper = Stan()
        helper.path = copy.deepcopy(stan.path)
        helper.currentCity = stan.currentCity
        helper.cost = stan.cost
        if i in helper.path:
            continue
        else:
            helper.addCost(calculateDistance(miasta[stan.currentCity][1], miasta[stan.currentCity][2], miasta[i][1], miasta[i][2]))
            helper.addPath(i)
            helper.setCurrentCity(i)
            listaStanow.append(helper)


    return listaStanow
