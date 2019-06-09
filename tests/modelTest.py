# Unit tests for model.py

import unittest
from model import *

currentGen = Grid(5, 5)
currentGen.__set__(0, 2, 1)
currentGen.__set__(0, 3, 1)
currentGen.__set__(3, 0, 1)
currentGen.__set__(3, 1, 1)
currentGen.__set__(4, 1, 1)
currentGen.__set__(4, 3, 1)
currentGen.__set__(4, 4, 1)
currentGen.__set__(3, 4, 1)
currentGen.__set__(2, 4, 1)

"""
Visual Representation of currentGen

0  0  1  1  0
0  0  0  0  0
0  0  0  0  1
1  1  0  0  1
0  1  0  1  1

"""


class TestModel(unittest.TestCase):

    # __scan__ tests
    def test_origin(self):
        self.assertEqual(currentGen.__scan__(0, 0), 0)

    def test_alive(self):
        self.assertEqual(currentGen.__scan__(0, 2), 1)

    def test_alive_right(self):
        self.assertEqual(currentGen.__scan__(0, 1), 1)

    def test_alive_left(self):
        self.assertEqual(currentGen.__scan__(0, 3), 1)

    def test_multi_rows(self):
        self.assertEqual(currentGen.__scan__(1, 0), 0)

    def test_multi_alive_multi_rows(self):
        self.assertEqual(currentGen.__scan__(4, 0), 3)

    def test_center(self):
        self.assertEqual(currentGen.__scan__(2, 2), 1)

    # __nextGen__ tests
    def test_three_adjacent_returns_alive(self):
        self.assertEqual(currentGen.__nextGen__(4, 0), 1)

    def test_two_adjacent_returns_alive(self):
        self.assertEqual(currentGen.__nextGen__(3, 0), 1)

    def test_one_adjacent_returns_dead(self):
        self.assertEqual(currentGen.__nextGen__(2, 2), 0)

    def test_four_adjacent_returns_dead(self):
        self.assertEqual(currentGen.__nextGen__(3, 3), 0)


if __name__ == '__main__':
    unittest.main()
