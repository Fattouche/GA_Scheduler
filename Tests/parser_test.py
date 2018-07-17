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


class TestingParser(unittest.TestCase):
    def test_parser(self):
        classes = parser.get_classes()
        students = parser.get_students()
        for class_id in classes:
            students_in_class = classes[class_id]
            for student in students_in_class:
                self.assertTrue(class_id in students[student])


if __name__ == '__main__':
    unittest.main()
