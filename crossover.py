from random import randint
from random import sample
import collections


def crossover(parent_1, parent_2, crossover=-1):
    length1 = len(parent_1)
    length2 = len(parent_2)
    if(length1 != length2):
        raise ValueError(
            'Parents differ in length. Parent_1 length: {0}, Parent_2 length: {1}'.format(length1, length2))
    crossover_point = randint(1, length1) if crossover == -1 else crossover
    crossover_keys = sample(parent_1.keys(), randint(1, length1))
    for key in crossover_keys:
        parent_1[key], parent_2[key] = parent_2[key], parent_1[key]
    return parent_1, parent_2


def population_crossover(population):
    for i in range(1, len(population)):
        population[i -
                   1], population[i] = crossover(population[i-1], population[i])
    return population


'''
TESTING:
classid: [room_id, timeslots, days]
parent1 = {1: ["1", ["1", "2"], "M"], 2: ["5", ["3", "8"], "F"], 3: [
    "27", ["14", "17"], "W"], 4: ["39", ["12", "14"], "S"]}
parent2 = {1: ["2", ["3", "4"], "T"], 2: ["94", ["18", "99"], "R"], 3: [
    "93", ["76", "72"], "SA"], 4: ["33", ["18", "196"], "S"]}
a, b = crossover(parent1, parent2)
print(a)
'''
