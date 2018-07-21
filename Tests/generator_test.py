import os
import sys
import unittest
import copy
import random

# Add parent directory to pathx
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import generator as gen
from helper import *


MAX_TIMESLOT = 27


class TestingGeneration(unittest.TestCase):

    def test_generation(self):
        room_ids = ROOM_INFO_DICT_1.keys()
        gene = gen.generate(room_ids)

        gene_len = len(gene)
        timeslot_len = len(gene[1])

        self.assertTrue(gene_len == 3)  # 3 things in gene
        self.assertTrue(timeslot_len == 2)  # 2 elements in timeslot
        self.assertTrue(gene[1][0] >= 0)  # first timeslot 0 or more
        # second timeslot less than max timeslot
        self.assertTrue(gene[1][1] <= MAX_TIMESLOT)
        self.assertTrue(gene[1][0] < gene[1][1])  # ending after beginin


if __name__ == '__main__':
    unittest.main()
