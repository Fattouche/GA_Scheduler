from random import randint
from random import sample
import os
import sys
sys.path.append(os.getcwd())
import generator


def mutate(parent):
    classes = sample(range(1, len(parent)), randint(1, len(parent)//100))
    for i in classes:
        parent[i] = generator.generate()

    return parent


def mutate_population(population):
    for chromosone in population:
        chromosone = mutate(chromosone)
    return population
