import os
import sys
import unittest

# Add parent directory to pathx
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fitness_function import FitnessCalculator
from helper import *


class TestFitnessFunction(unittest.TestCase):
    def test_total_room_overflow_zero(self):
        fitness_calculator = FitnessCalculator(
            ROOM_INFO_DICT_1, 
            COURSE_STUDENTS_DICT_1,
            None, None
        )

        total_room_overflow = fitness_calculator.calc_total_room_overflow(
            CHROMOSOME_1
        )
        self.assertEqual(total_room_overflow, 0)

    def test_total_room_overflow_positive(self):
        fitness_calculator = FitnessCalculator(
            ROOM_INFO_DICT_1, 
            COURSE_STUDENTS_DICT_1,
            None, None
        )

        total_room_overflow = fitness_calculator.calc_total_room_overflow(
            CHROMOSOME_2
        )

        self.assertEqual(total_room_overflow, 3)

    def test_student_course_conflicts_zero(self):
        fitness_calculator = FitnessCalculator(
            None, None,
            STUDENT_COURSES_DICT_1, None
        )

        num_student_course_conflicts = \
            fitness_calculator.calc_num_student_course_conflicts(
                CHROMOSOME_1
            )

        self.assertEqual(num_student_course_conflicts, 0)

    def test_student_course_conflicts_positive(self):
        fitness_calculator = FitnessCalculator(
            None, None,
            STUDENT_COURSES_DICT_1, None
        )

        num_student_course_conflicts = \
            fitness_calculator.calc_num_student_course_conflicts(
                CHROMOSOME_2
            )

        self.assertEqual(num_student_course_conflicts, 1)

        num_student_course_conflicts = \
            fitness_calculator.calc_num_student_course_conflicts(
                CHROMOSOME_3
            )

        self.assertEqual(num_student_course_conflicts, 3)

    def test_unfavoured_timeslots_zero(self):
        fitness_calculator = FitnessCalculator(None, None, None, None)

        num_unfavoured_timeslots = \
            fitness_calculator.calc_num_unfavoured_timeslots_used(
                CHROMOSOME_1
            )

        self.assertEqual(num_unfavoured_timeslots, 0)

    def test_unfavoured_timeslots_positive(self):
        fitness_calculator = FitnessCalculator(None, None, None, None)

        num_unfavoured_timeslots = \
            fitness_calculator.calc_num_unfavoured_timeslots_used(
                CHROMOSOME_4
            )

        self.assertEqual(num_unfavoured_timeslots, 3)

    def test_num_empty_seats_1(self):
        fitness_calculator = FitnessCalculator(
            ROOM_INFO_DICT_1, 
            COURSE_STUDENTS_DICT_1,
            None, None
        )

        num_empty_seats = \
            fitness_calculator.calc_num_empty_seats_in_course_rooms(
                CHROMOSOME_5
            )

        self.assertEqual(num_empty_seats, 7)

    def test_num_empty_seats_2(self):
        fitness_calculator = FitnessCalculator(
            ROOM_INFO_DICT_1, 
            COURSE_STUDENTS_DICT_1,
            None, None
        )

        num_empty_seats = \
            fitness_calculator.calc_num_empty_seats_in_course_rooms(
                CHROMOSOME_6
            )

        self.assertEqual(num_empty_seats, 7)

    def test_num_course_room_time_conflicts_zero(self):
        fitness_calculator = FitnessCalculator(
            None, None, None, None
        )

        num_course_room_time_conflicts = \
            fitness_calculator.calc_num_course_room_time_conflicts(CHROMOSOME_7)
        
        self.assertTrue(num_course_room_time_conflicts == 0)

    def test_num_course_room_time_conflicts_positive(self):
        fitness_calculator = FitnessCalculator(
            None, None, None, None
        )

        num_course_room_time_conflicts = \
            fitness_calculator.calc_num_course_room_time_conflicts(CHROMOSOME_8)

        self.assertTrue(num_course_room_time_conflicts == 2)


if __name__ == '__main__':
    unittest.main()
