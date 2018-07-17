import os
import sys
import unittest
import copy
import random

sys.path.append("..")
import crossover as crosser
from helper import *


MAX_TIMESLOT = 27


class TestingCrossover(unittest.TestCase):
    def test_crossover(self):
        parent1, parent2 = CHROMOSOME_1, CHROMOSOME_2
        crossover_keys = [1, 2]
        leftover_keys = [3]

        copyp1 = copy.deepcopy(parent1)
        copyp2 = copy.deepcopy(parent2)
        parent1, parent2 = crosser.crossover(
            parent1, parent2, crossover_keys)

        first_part_p1 = True
        second_part_p1 = True
        first_part_p2 = True
        second_part_p2 = True

        # Parent1 check
        # before crossover point same as parent1
        for i in crossover_keys:
            if parent1[i] != copyp2[i]:
                first_part_p1 = False

        # after crossover point same as parent2
        for i in leftover_keys:
            if parent1[i] != copyp1[i]:
                second_part_p1 = False

       # Parent1 check
        # before crossover point same as parent1
        for i in crossover_keys:
            if parent2[i] != copyp1[i]:
                first_part_p2 = False

        # after crossover point same as parent2
        for i in leftover_keys:
            if parent2[i] != copyp2[i]:
                second_part_p2 = False

        self.assertTrue(first_part_p1)
        self.assertTrue(second_part_p1)
        self.assertTrue(first_part_p2)
        self.assertTrue(second_part_p2)


if __name__ == '__main__':
    unittest.main()
