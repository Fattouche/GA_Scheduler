from random import randint
from random import sample
import os
import sys
import math

import generator


def mutate(parent, room_ids, divisor=100):
    classes = sample(parent.keys(), randint(1, math.ceil(len(parent) / divisor)))
    for i in classes:
        parent[i] = generator.generate(room_ids)

    return parent


def mutate_population(population, room_ids):
    for chromosome in population:
        chromosome = mutate(chromosome, room_ids)
    return population
