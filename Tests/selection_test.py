import os
import sys
import unittest
import copy
import random

sys.path.append("..")
import selection as selector
from fitness_function import FitnessCalculator
from helper import *


MAX_TIMESLOT = 27


class TestingSelection(unittest.TestCase):
    def test_selection(self):
        fitness_calculator = FitnessCalculator(
            ROOM_INFO_DICT_1, 
            COURSE_STUDENTS_DICT_1,
            STUDENT_COURSES_DICT_1, None
        )

        selection = selector.selection(population, fitness_calculator)

        self.assertEqual(len(selection), len(population))


if __name__ == '__main__':
    unittest.main()
