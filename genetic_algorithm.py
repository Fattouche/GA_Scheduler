import generator
import selection as selector
import mutate as mutator
import fitness_function as fitness_helper
import crossover
import xml_parser as parser

POPULATION_SIZE = 100

course_students_dict = parser.get_classes()
room_information_dict = parser.get_rooms()
student_courses_dict = parser.get_students()
room_ids = list(room_information_dict.keys())


def seed_population(population_size):
    population = []
    for i in range(population_size):
        population.append(generator.get_chromosome(
            course_students_dict, room_ids))
    return population


def preform_genetic_algorithm():
    population = seed_population(POPULATION_SIZE)
    while(True):
        print("Beginning new selection")
        population = selector.selection(
            population, room_information_dict, course_students_dict, student_courses_dict)
        population = crossover.population_crossover(population)
        population = mutator.mutate_population(population, room_ids)
        fittest_chromosome = fitness_helper.fittest_chromosome(
            population, room_information_dict,
            course_students_dict, student_courses_dict)
        if fitness_helper.is_valid(fittest_chromosome, room_information_dict,
                                   course_students_dict, student_courses_dict):
            return fittest_chromosome
    return None


def main():
    chromosome = preform_genetic_algorithm()
    print("Finished calculating")
    print(chromosome)


if __name__ == "__main__":
    main()
