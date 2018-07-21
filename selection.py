import random
import copy

from fitness_function import FitnessCalculator


# Returns a list of individuals to participate in crossover, selected
# with probability proportional to their fitness
# The number of individuals returned is the same as the population size
def selection(population, fitness_calculator):
    fitnesses = [fitness_calculator.calc_fitness(individual) for individual in population]

    # min_fitness = min(fitnesses)

    # # A simple way to scale up the value of better fitnesses (if fitnesses
    # # are all very large, we will get weights that are too similar to each other)
    # fitnesses_normalized = [fitness - min_fitness + 1 for fitness in fitnesses]

    # Want to minimize fitness, so use inverse fitnesses as the weights
    inverse_fitnesses = [1.0 / fitness for fitness in fitnesses]

    selection = random.choices(population, weights=inverse_fitnesses, k=len(population))

    # Need to return deepcopies! Otherwise crossover/mutation will affect all
    # individuals that were duplicated during selection
    return [copy.deepcopy(individual) for individual in selection]
