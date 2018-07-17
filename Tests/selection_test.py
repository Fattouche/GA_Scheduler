import os
import sys
import unittest
import copy
import random

sys.path.append("..")
import selection as selector
from helper import *


MAX_TIMESLOT = 27


class TestingSelection(unittest.TestCase):
    def test_selection(self):
        selection = selector.selection(
            population, ROOM_INFO_DICT_1, COURSE_STUDENTS_DICT_1, STUDENT_COURSES_DICT_1)
        self.assertEqual(len(selection), len(population))


if __name__ == '__main__':
    unittest.main()
