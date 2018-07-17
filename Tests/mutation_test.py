import os
import sys
import unittest
import copy
import random

sys.path.append("..")
import mutate as mutator
from helper import *


MAX_TIMESLOT = 27


class TestingMutation(unittest.TestCase):

    def test_mutation(self):
        room_ids = list(ROOM_INFO_DICT_1)
        chromosome = CHROMOSOME_1
        copy_chromosome = copy.deepcopy(chromosome)
        self.assertEqual(chromosome, copy_chromosome)
        chromosome = mutator.mutate(chromosome, room_ids, 1)
        self.assertNotEqual(chromosome, copy_chromosome)
        for gene in chromosome.values():
            gene_len = len(gene)
            timeslot_len = len(gene[1])
            self.assertTrue(gene_len == 3)  # 3 things in gene
            self.assertTrue(timeslot_len == 2)  # 2 elements in timeslot
            self.assertTrue(gene[1][0] >= 0)  # first timeslot 0 or more
            # second timeslot less than max timeslot
            self.assertTrue(gene[1][1] <= MAX_TIMESLOT)
            self.assertTrue(gene[1][0] < gene[1][1])  # ending after begining


if __name__ == '__main__':
    unittest.main()
