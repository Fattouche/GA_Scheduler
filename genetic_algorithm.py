import generator
import selection as selector
import mutate as mutator
import fitness_function as fitness
import crossover

POPULATION_SIZE = 100
FITNESS_THRESHOLD = 0


def seed_population(population_size):
    population = []
    for i in range(population_size):
        population.append(generator.get_chromosome())
    return population


def algorize():
    population = seed_population(POPULATION_SIZE)
    while(True):
        population = selector.selection(population)
        population = crossover.population_crossover(population)
        population = mutator.mutate_population(population)
        if fitness.calc_fit(population) > 0:
            break
    return population
