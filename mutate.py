from random import randint
from random import sample
import os
import sys
sys.path.append(os.getcwd())
import chromosome_generator as generator


def mutate(parent):
    classes = sample(range(1, len(parent)), randint(1, len(parent)//2))
    for i in classes:
        parent[i] = generator.generate()

    return parent

    
