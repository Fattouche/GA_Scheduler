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
parser.add_argument('fitness_threshold', type=int, help='Fitness value below which chromosomes will be accepted (want to minimize fitness value).')

args = parser.parse_args()


def seed_population(population_size, course_students_dict, room_ids):
    population = []
    for i in range(population_size):
        population.append(generator.get_chromosome(
            course_students_dict, room_ids))
    return population


def preform_genetic_algorithm(input_file, fitness_threshold):
    parser = Parser(input_file)

    room_information_dict, course_students_dict, student_courses_dict, _ = parser.parse_input()

    room_ids = list(room_information_dict.keys())

    population = seed_population(POPULATION_SIZE, course_students_dict, room_ids)

    fitness_calculator = FitnessCalculator(room_information_dict, course_students_dict,
                                            student_courses_dict, fitness_threshold)

    while(True):
        print("Beginning new selection")
        population = selector.selection(population, fitness_calculator)
        population = crossover.population_crossover(population)
        population = mutator.mutate_population(population, room_ids)
        fittest_chromosome = fitness_calculator.fittest_chromosome(population)

        if fitness_calculator.is_valid(fittest_chromosome):
            return fittest_chromosome, fitness_calculator.calc_fitness(fittest_chromosome)
    return None


if __name__ == "__main__":
    chromosome = preform_genetic_algorithm(args.input_file, args.fitness_threshold)
    print("Finished calculating")
    print(chromosome)
