from random import randint
from random import sample


def mutate(parent):
    classes = sample(range(1, len(parent)), randint(1, len(parent)//2))
    # Run when generate exists
    # for i in classes:
    #     parent[i] = generate()
    # retu.rn parent
