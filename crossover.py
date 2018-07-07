from random import randint
import collections


def crossover(parent_1, parent_2):
    length1 = len(parent_1)
    length2 = len(parent_2)
    if(length1 != length2):
        raise ValueError(
            'Parents differ in length. Parent_1 length: {0}, Parent_2 length: {1}'.format(length1, length2))
    for i in range(randint(1, length1), length1+1):
        parent_1[i], parent_2[i] = parent_2[i], parent_1[i]
    return parent_1, parent_2


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
