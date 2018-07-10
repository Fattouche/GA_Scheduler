import random

import fitness_function as fitness_helper


# Returns a list of individuals to participate in crossover, selected
# with probability proportional to their fitness
# The number of individuals returned is the same as the population size
def selection(population, room_information_dict,
              course_students_dict, student_courses_dict):
    fitnesses = [fitness_helper.calc_fitness(
        individual, room_information_dict,
                 course_students_dict, student_courses_dict, ) for individual in population]

    return random.choices(population, weights=fitnesses, k=len(population))
