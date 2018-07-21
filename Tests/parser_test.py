import os
import sys
import unittest
import copy
import random

sys.path.append("..")
import generator as gen
import mutate as mutator
import crossover as crosser
from xml_parser import Parser


MAX_TIMESLOT = 27


class TestingParser(unittest.TestCase):
    def setUp(self):
        self.input_file = '../data/purdue_math_dataset/input.xml'

    def test_parser(self):
        parser = Parser(self.input_file)

        rooms, classes, students, class_map = parser.parse_input()

        for class_id in classes:
            students_in_class = classes[class_id]
            for student in students_in_class:
                self.assertTrue(class_id in students[student])


if __name__ == '__main__':
    unittest.main()
