import os
import sys
import unittest
from collections import defaultdict

# Add parent directory to pathx
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fitness_function


ROOM_INFO_DICT_1 = {
  1: {"capacity": "5"},
  2: {"capacity": "8"},
  3: {"capacity": "10"}
}

STUDENT_COURSES_DICT_1 = {
  1: [1],
  2: [1],
  3: [1],
  4: [1],
  5: [1, 2],
  6: [1, 2],
  7: [1, 2],
  8: [2],
  9: [3],
  10: [3, 1],
  11: [3, 2]
}

COURSES_STUDENTS_DICT_1 = defaultdict(set)
for key, value in STUDENT_COURSES_DICT_1.items():
  for course in value:
    COURSES_STUDENTS_DICT_1[course].add(key)

print("COURSES_STUDENT_DICT_1: {}".format(COURSES_STUDENTS_DICT_1))

CHROMOSOME_1 = {
  1: [1, [4, 6], 'MW'],
  2: [2, [4, 6], 'TH'],
  3: [3, [4, 6], 'WF']
}

CHROMOSOME_2 = {
  1: [2, [4, 6], 'MW'],
  2: [1, [4, 6], 'TH'],
  3: [3, [4, 6], 'WF']
}


class TestFitnessFunction(unittest.TestCase):

  def test_total_room_overflow_positive(self):
    total_room_overflow = fitness_function.calc_total_room_overflow(
      CHROMOSOME_1, ROOM_INFO_DICT_1, COURSES_STUDENTS_DICT_1
    )

    assertEquals(total_room_overflow, 2)

  def test_total_room_overflow_zero(self):
    total_room_overflow = fitness_function.calc_total_room_overflow(
      CHROMOSOME_2, ROOM_INFO_DICT_1, COURSES_STUDENTS_DICT_1
    )

    assertEquals(total_room_overflow, 0)