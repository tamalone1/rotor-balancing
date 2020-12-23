# -*- coding: utf-8 -*-
"""
MIT License

Copyright (c) 2020 tamalone1
"""

import unittest
from rotor_balancing import Vector, balance_one_plane


class TestRotor(unittest.TestCase):

    def test_placeholder(self):
        self.assertTrue(True)


class TestOnePlane(unittest.TestCase):

    def test_oneplane(self):
        # Single component input
        input_ = [Vector(1, 0, 0)]
        balance = balance_one_plane(input_)
        self.assertEqual(balance, Vector(-1, 0, 0))
        # Two perpendicular components input
        input_ = [Vector(1, 0, 0), Vector(0, 1, 0)]
        balance = balance_one_plane(input_)
        self.assertEqual(balance, Vector(-1, -1, 0))


class TestVector(unittest.TestCase):

    def test_equality(self):
        vector1 = Vector(1, 2, 3)
        vector2 = Vector(1, 2, 4)
        self.assertEqual(vector1, Vector(1, 2, 3))
        self.assertNotEqual(vector1, vector2)


if __name__ == '__main__':
    unittest.main()
