from random import randint
from random import sample
import os
import sys
sys.path.append(os.getcwd())
import generator


def mutate(parent, room_ids, divisor=100):
    classes = sample(parent.keys(), randint(1, len(parent)//divisor))
    for i in classes:
        parent[i] = generator.generate(room_ids)

    return parent


def mutate_population(population, room_ids):
    for chromosone in population:
        chromosone = mutate(chromosone, room_ids)
    return population
