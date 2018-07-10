import os
import sys
import unittest
from collections import defaultdict

# Add parent directory to pathx
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import fitness_function


ROOM_INFO_DICT_1 = {
  1: {"capacity": 5},
  2: {"capacity": 8},
  3: {"capacity": 10}
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

COURSE_STUDENTS_DICT_1 = defaultdict(set)
for key, value in STUDENT_COURSES_DICT_1.items():
  for course in value:
    COURSE_STUDENTS_DICT_1[course].add(key)

CHROMOSOME_1 = {
  1: [2, [4, 6], 'MW'],
  2: [1, [7, 9], 'TR'],
  3: [3, [10, 12], 'WF']
}

CHROMOSOME_2 = {
  1: [1, [4, 6], 'MW'],
  2: [2, [4, 6], 'TR'],
  3: [3, [4, 6], 'WF']
}

CHROMOSOME_3 = {
  1: [1, [6, 8], 'MW'],
  2: [2, [5, 6], 'MTR'],
  3: [3, [9, 11], 'WF']
}

CHROMOSOME_4 = {
  1: [1, [1, 3], 'MW'],
  2: [2, [5, 6], 'MTR'],
  3: [3, [9, 11], 'WF']
}

CHROMOSOME_5 = {
  1: [2, [4, 6], 'MW'],
  2: [1, [4, 6], 'MW'],
  3: [3, [4, 6], 'MW']
}

CHROMOSOME_6 = {
  1: [3, [4, 6], 'MW'],
  2: [2, [4, 6], 'MW'],
  3: [1, [4, 6], 'MW']
}


CHROMOSOME_7 = {
  1: [1, [1, 3], 'MW'],
  2: [1, [4,6], 'MW'],
  3: [1, [1, 3], 'TR']
}

CHROMOSOME_8 = {
  1: [1, [1, 3], 'MW'],
  2: [1, [3, 6], 'MW'],
  3: [1, [1, 3], 'TR']
}


class TestFitnessFunction(unittest.TestCase):
  def test_total_room_overflow_zero(self):
    total_room_overflow = fitness_function.calc_total_room_overflow(
      CHROMOSOME_1, ROOM_INFO_DICT_1, COURSE_STUDENTS_DICT_1
    )

    self.assertEqual(total_room_overflow, 0)

  def test_total_room_overflow_positive(self):
    total_room_overflow = fitness_function.calc_total_room_overflow(
      CHROMOSOME_2, ROOM_INFO_DICT_1, COURSE_STUDENTS_DICT_1
    )

    self.assertEqual(total_room_overflow, 3)

  def test_student_course_conflicts_zero(self):
    num_student_course_conflicts = \
      fitness_function.calc_num_student_course_conflicts(
        CHROMOSOME_1, STUDENT_COURSES_DICT_1
      )

    self.assertEqual(num_student_course_conflicts, 0)

  def test_student_course_conflicts_positive(self):
    num_student_course_conflicts = \
      fitness_function.calc_num_student_course_conflicts(
        CHROMOSOME_2, STUDENT_COURSES_DICT_1
      )

    self.assertEqual(num_student_course_conflicts, 1)

    num_student_course_conflicts = \
      fitness_function.calc_num_student_course_conflicts(
        CHROMOSOME_3, STUDENT_COURSES_DICT_1
      )

    self.assertEqual(num_student_course_conflicts, 3)

  def test_unfavoured_timeslots_zero(self):
    num_unfavoured_timeslots = \
      fitness_function.calc_num_unfavoured_timeslots_used(
        CHROMOSOME_1
      )

    self.assertEqual(num_unfavoured_timeslots, 0)

  def test_unfavoured_timeslots_positive(self):
    num_unfavoured_timeslots = \
      fitness_function.calc_num_unfavoured_timeslots_used(
        CHROMOSOME_4
      )

    self.assertEqual(num_unfavoured_timeslots, 3)

  def test_num_empty_seats_1(self):
    num_empty_seats = \
      fitness_function.calc_num_empty_seats_in_course_rooms(
        CHROMOSOME_5, ROOM_INFO_DICT_1, COURSE_STUDENTS_DICT_1
      )

    self.assertEqual(num_empty_seats, 7)

  def test_num_empty_seats_2(self):
    num_empty_seats = \
      fitness_function.calc_num_empty_seats_in_course_rooms(
        CHROMOSOME_6, ROOM_INFO_DICT_1, COURSE_STUDENTS_DICT_1
      )

    self.assertEqual(num_empty_seats, 7)

  def test_num_course_room_time_conflicts_zero(self):
    num_course_room_time_conflicts = fitness_function.calc_num_course_room_time_conflicts(CHROMOSOME_7)
    self.assertTrue(num_course_room_time_conflicts == 0)


  def test_num_course_room_time_conflicts_positive(self):
    num_course_room_time_conflicts = fitness_function.calc_num_course_room_time_conflicts(CHROMOSOME_8)
    self.assertTrue(num_course_room_time_conflicts == 2)


if __name__ == '__main__':
    unittest.main()
