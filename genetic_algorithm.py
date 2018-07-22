import argparse

import generator
import selection as selector
import mutate as mutator
from fitness_function import FitnessCalculator
import crossover
from xml_parser import Parser

POPULATION_SIZE = 100

parser = argparse.ArgumentParser(description='Genetic algorithm for developing a timetable schedule.')
parser.add_argument('input_file', type=str,
                    help='XML file that defines classes, students and rooms.')
parser.add_argument('fitness_threshold', type=float, help='Fitness value below which chromosomes will be accepted (want to minimize fitness value).')
parser.add_argument('--round_limit', type=int, default=0, help='Maximum number of selection rounds to\
                        execute. If set to 0, will run indefinitely (or until a\
                        solution is reached.')

args = parser.parse_args()


def seed_population(population_size, course_students_dict, room_ids):
    population = []
    for i in range(population_size):
        population.append(generator.get_chromosome(
            course_students_dict, room_ids))
    return population


def preform_genetic_algorithm(input_file, fitness_threshold, round_limit):
    parser = Parser(input_file)

    room_information_dict, course_students_dict, student_courses_dict, _ = parser.parse_input()

    room_ids = list(room_information_dict.keys())

    population = seed_population(POPULATION_SIZE, course_students_dict, room_ids)

    fitness_calculator = FitnessCalculator(room_information_dict, course_students_dict,
                                            student_courses_dict, fitness_threshold)

    rounds = 1
    min_fitness = float('inf')

    
    while rounds <= round_limit or round_limit == 0:
        print("Beginning new selection")
        population = selector.selection(population, fitness_calculator)

        # print('population after selection:')
        # for individual in population:
        #     print(individual)
        #     print('***')
        # print('end population')

        population = crossover.population_crossover(population)

        # print('population after crossover:')
        # for individual in population:
        #     print(individual)
        #     print('***')
        # print('end population')

        population = mutator.mutate_population(population, room_ids)

        # print('population after mutation:')
        # for individual in population:
        #     print(individual)
        #     print('***')
        # print('end population')

        fit_chromosomes = fitness_calculator.get_fit_chromosomes(population)

        # distinct_individuals = []
        # for individual in population:
        #     if individual not in distinct_individuals:
        #         distinct_individuals.append(individual)
        # print('Num distinct individuals after mutation: {}'.format(len(distinct_individuals)))

        if fit_chromosomes:
            print('Num fit chromosomes: {}'.format(len(fit_chromosomes)))

        for chromosome, fitness, validity in fit_chromosomes:
            min_fitness = min(min_fitness, fitness)
            
            if validity == True:
                return chromosome, fitness, rounds

        rounds += 1

    print('Failed. Min fitness found: {}'.format(min_fitness))
    return None


if __name__ == "__main__":
    result = preform_genetic_algorithm(args.input_file, args.fitness_threshold,
        args.round_limit)
    print("Finished calculating")
    if result:
        print('chromosome: {}'.format(result[0]))
        print('fitness: {}'.format(result[1]))
        print('rounds: {}'.format(result[2]))
