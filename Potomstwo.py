import copy
import math

from Stan import Stan


def calculateDistance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return dist


def potomstwo(stan, miasta):
    howMany = len(miasta)

    if len(stan.path) >= howMany:
        return -1

    listaStanow = []

    for i in range(howMany):

        temp = Stan(stan.currentCity, stan.path,stan.cost)
        if i in temp.path:
            continue
        else:
            temp.cost += math.sqrt(
                (miasta[i][1] - miasta[stan.currentCity][1]) ** 2 + (miasta[i][2] - miasta[stan.currentCity][2]) ** 2)
            temp.path.append(i)
            temp.currentCity = i
            listaStanow.append(temp)


    return listaStanow
