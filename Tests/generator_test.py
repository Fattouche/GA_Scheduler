import os
import sys
import unittest
import copy
import random

sys.path.append("..")
import generator as gen
import mutate as mutator
import crossover as crosser
import xml_parser as parser


MAX_TIMESLOT = 27


class TestingMutationAndCrossover(unittest.TestCase):

    def test_parser(self):
        classes = parser.get_classes()
        students = parser.get_students()
        for class_id in classes:
            students_in_class = classes[class_id]
            for student in students_in_class:
                self.assertTrue(class_id in students[student])

    def test_generation(self):
        gene = gen.generate()
        gene_len = len(gene)
        timeslot_len = len(gene[1])

        self.assertTrue(gene_len == 3)  # 3 things in gene
        self.assertTrue(timeslot_len == 2)  # 2 elements in timeslot
        self.assertTrue(gene[1][0] >= 0)  # first timeslot 0 or more
        # second timeslot less than max timeslot
        self.assertTrue(gene[1][1] <= MAX_TIMESLOT)
        self.assertTrue(gene[1][0] < gene[1][1])  # ending after begining

    def test_mutation(self):
        parent = gen.get_chromosome()
        copy1 = copy.deepcopy(parent)
        num_changed = 0
        runs = 10

        for i in range(runs):
            mutated = mutator.mutate(parent)
            for class_id in copy1:
                if copy1[class_id] != mutated[class_id]:
                    num_changed += 1

        self.assertTrue(num_changed > 0)

    def test_crossover(self):
        first_part_p1 = True
        second_part_p2 = True

        parent1 = gen.get_chromosome()
        parent2 = gen.get_chromosome()
        crossover_point = random.randint(1, len(parent1))

        copyp1 = copy.deepcopy(parent1)
        parent1, parent2 = crosser.crossover(parent1, parent2, crossover_point)

        # before crossover point same as parent1
        for i in range(1, crossover_point):
            if copyp1[i] != parent1[i]:
                first_part_p1 = False

        # after crossover point same as parent2
        for i in range(crossover_point, len(parent1)+1):
            if copyp1[i] != parent2[i]:
                second_part_p2 = False

        self.assertTrue(first_part_p1)
        self.assertTrue(second_part_p2)


if __name__ == '__main__':
    unittest.main()
