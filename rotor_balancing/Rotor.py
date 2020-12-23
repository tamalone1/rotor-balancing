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
        self.test_mass_left_plane = {}
        self.test_mass_right_plane = {}

    def add_imbalance(self, mass_radius, phase):
        """Add a mass-radius couple at a particular phase angle."""
        pass

    @staticmethod
    def get_stiffnesses(XAm, XBm, XA, XB, m):
        """ Find the stiffnesses in each balance plane due to trial masses."""
        A = (XAm - XA)/m
        B = (XBm - XB)/m
        return A, B

    @staticmethod
    def required_balances(AL, BL, AR, BR, XA, XB):
        """ Find the required balances to add to balance the rotor."""
        ML = (XA*BR-AR*XB)/(AL*BR-AR*BL)
        MR = (AL*XB-XA*BL)/(AL*BR-AR*BL)
        return ML, MR

    def add_left_test_mass(self, deflection_A, deflection_B, mL):
        """ Add the deflections caused by the left deflection mass. """
        self.test_mass_left_plane = {'XAL': deflection_A,
                                     'XBL': deflection_B,
                                     'mL': mL}

    def add_right_test_mass(self, deflection_A, deflection_B, mR):
        """ Add the deflections caused by the right deflection mass. """
        self.test_mass_right_plane = {'XAR': deflection_A,
                                      'XBR': deflection_B,
                                      'mR': mR}

    def solve(self):
        """ Find the required balance masses in each balance plane."""
        # Procedure:
        # Calculate the stiffness of the rotor relative to the test masses,
        # placed at each balancing plane. Using the stiffnesses, calculate the
        # balance mass that will result in zero deflections at the bearings.
        XAL, XBL, mL = self.test_mass_left_plane.values()
        XAR, XBR, mR = self.test_mass_right_plane.values()
        XA, XB = self.baseline.values()
        left_stiffnesses = self.get_stiffnesses(XAL, XBL, XA, XB, mL)
        right_stiffnesses = self.get_stiffnesses(XAR, XBR, XA, XB, mR)
        # The existing unbalances and their locations, on planes L and R
        ML, MR = self.required_balances(*left_stiffnesses,
                                        *right_stiffnesses,
                                        XA,
                                        XB)
        return ML, MR
