# -*- coding: utf-8 -*-
"""

Copyright (c) 2020 tamalone1
"""
import cmath
from math import radians

# Basic single plane balancing: add up the centrifugal force vectors from the
# imbalanced masses, and the resultant is the negative of the required force
# vector. This is enough to static balancing, and a basic chunk for dynamic 
# balancing. Need: add a number of 2D vectors in a plane. 
# Should the Vector class be 3D?
# Should the Vector be xyz coordinates or R-theta?

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'

    def __add__(self, other):
        """ Add by components, and return a new Vector. """
        # Check if the other parameter is a Vector or a scalar
        if isinstance(other, Vector):
            # the parameter is a Vector, add the components
            xf = self.x + other.x
            yf = self.y + other.y
            zf = self.z + other.z
        else:
            return NotImplemented
        return Vector(xf, yf, zf)

    def __sub__(self, other):
        """ Subtract by components, and return a new Vector. """
        # Check if the other parameter is a Vector or a scalar
        if isinstance(other, Vector):
            # the parameter is a Vector, subtract the components
            xf = self.x - other.x
            yf = self.y - other.y
            zf = self.z - other.z
        else:
            return NotImplemented
        return Vector(xf, yf, zf)

    def __mul__(self, other):
        """ Multiply by components, and return a new Vector. """
        # Check if the other parameter is a Vector or a scalar
        if isinstance(other, Vector):
            # the parameter is a Vector, multiply each component pair
            xf = self.x * other.x
            yf = self.y * other.y
            zf = self.z * other.z
        else:
            return NotImplemented
        return Vector(xf, yf, zf)

    def __neg__(self):
        ''' Return the equal and opposite direction Vector. '''
        xf = self.x * -1
        yf = self.y * -1
        zf = self.z * -1
        return Vector(xf, yf, zf)


def balance_one_plane(vectors):
    ''' Get the balancing vector needed to balance in a single plane.

    Inputs:
    vectors: sequence of Vector objects representing imbalance masses (x, y, z)
    
    Returns:
    result: Vector equal and opposite to the sum of the input Vectors
    '''
    # add up the input vectors
    result = Vector(0, 0, 0)
    for i in vectors:
        result = result + i
    # return the negative of the sum
    return -result

# Basic 3D balancing: choose two balancing planes where balance masses will be
# added. Multiply each centrifugal force vector by the axial distance from one
# of the chosen planes. With those scaled vectors, find the balance mass for the
# other balancing plane, scaled likewise by the distance between the planes. 
# With the known imbalances and the first balancing mass, balance the remaining
# balancing plane. 


def bearing_reactions():
    ''' Calculate bearing reactions caused by imbalances.
    
    inputs:
    imbalances: group of mass-radius products causing imbalance
    bearing separation length
    axial position of each imbalance, as z-coordinate
    rotation speed: rad/s, about the z-axis

    Outputs:
    reaction forces at each bearing (vectors in xy-plane)
    '''
    pass

''' See section 17.8 of Theory of Machines and Mechanisms, 4th ed.:
Field Balancing with a Programmable Calculator.
Complex numbers are used in the form x+yj or Re^jt. Both can be handled easily 
with the builtin complex method and the cmath module.
Unbalances cause reaction forces at each bearing 
These are measured as X = X*e^jt for two bearings A and B
Procedure:
1. In first run, measure baseline reaction forces at each bearing 
'''

def get_stiffnesses(XAm, XBm, XA, XB, m):
    ''' Find the stiffnesses in each balance plane due to trial masses.'''
    A = (XAm - XA)/m
    B = (XBm - XB)/m
    return A, B


def required_balances(AL, BL, AR, BR, XA, XB):
    ''' Find the required balances to add to balance the rotor.'''
    ML = (XA*BR-AR*XB)/(AL*BR-AR*BL)
    MR = (AL*XB-XA*BL)/(AL*BR-AR*BL)
    return ML, MR
