# -*- coding: utf-8 -*-
"""

Copyright (c) 2020 tamalone1
"""
import cmath
from math import radians


class Rotor:

    def __init__(self, bearing_deflection_A, bearing_deflection_B):
        # Required data: bearing deflections, imbalanced masses
        self.baseline = {'XA': bearing_deflection_A,
                         'XB': bearing_deflection_B}
        self.test_mass_1 = {}
        self.test_mass_2 = {}

    def add_imbalance(self, mass_radius, phase):
        '''Add a mass-radius couple at a particular phase angle.'''
        pass

    @staticmethod
    def get_stiffnesses(XAm, XBm, XA, XB, m):
        ''' Find the stiffnesses in each balance plane due to trial masses.'''
        A = (XAm - XA)/m
        B = (XBm - XB)/m
        return A, B

    @staticmethod
    def required_balances(AL, BL, AR, BR, XA, XB):
        ''' Find the required balances to add to balance the rotor.'''
        ML = (XA*BR-AR*XB)/(AL*BR-AR*BL)
        MR = (AL*XB-XA*BL)/(AL*BR-AR*BL)
        return ML, MR

    def solve(self):
        ''' Find the required balance masses in each balance plane.'''
        # Procedure:
        # Calculate the stiffness of the rotor relative to the test masses,
        # placed at each balancing plane. Using the stiffnesses, calculate the
        # balance mass that will result in zero deflections at the bearings.
        pass
