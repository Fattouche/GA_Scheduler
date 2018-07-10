import generator
import selection as selector
import mutate as mutator
import fitness_function as fitness
import crossover
import xml_parser as parser

POPULATION_SIZE = 100
FITNESS_THRESHOLD = -50
class_information_dict = parser.get_classmap()
room_information_dict = parser.get_rooms()
student_information_dict = parser.get_students()
room_id_list = list(room_information_dict.keys())


def seed_population(population_size):
    population = []
    for i in range(population_size):
        population.append(generator.get_chromosome(
            class_information_dict, room_id_list))
    return population


def main():
    population = seed_population(POPULATION_SIZE)
    while(True):
        population = selector.selection(population)
        population = crossover.population_crossover(population)
        population = mutator.mutate_population(population)
        if fitness.calc_fit(population) > FITNESS_THRESHOLD and fitness.is_population_valid(population, room_information_dict, student_information_dict, course_information_dict):
            break
    return population


if __name__ == "__main__":
    main()
