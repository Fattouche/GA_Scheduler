import random

from fitness_function import fitness_function


# Returns a list of individuals to participate in crossover, selected
# with probability proportional to their fitness
# The number of individuals returned is the same as the population size
def selection(population):
  fitnesses = [fitness_function(individual) for individual in population]

  return random.choices(population, weights=fitnesses, k=len(population))
