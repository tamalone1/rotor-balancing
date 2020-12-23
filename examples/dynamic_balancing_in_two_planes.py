# -*- coding: utf-8 -*-
"""

Copyright (c) 2020 tamalone1
"""
import cmath
from math import radians
from rotor_balancing.Rotor import Rotor

# Baseline reactions (length)
XA = cmath.rect(8.6, radians(63))
XB = cmath.rect(6.5, radians(206))
# Create Rotor instance with baseline reactions motions
rotor = Rotor(XA, XB)
# Trial masses and locations (mg-m) on planes L and R respectively
mL = cmath.rect(10, radians(270))
mR = cmath.rect(12, radians(180))
# Trial reactions using mL on plane L (length)
XAL = cmath.rect(5.9, radians(123))
XBL = cmath.rect(4.5, radians(228))
rotor.add_left_test_mass(XAL, XBL, mL)
# Trial reactions using mR on plane R (length)
XAR = cmath.rect(6.2, radians(36))
XBR = cmath.rect(10.4, radians(162))
rotor.add_right_test_mass(XAR, XBR, mR)
# The existing unbalances and their locations, on planes L and R
ML, MR = rotor.solve()
# Print the result in polar form like the problem statement
print('ML: {:>7.03f} < {:> 4.03f}'.format(*cmath.polar(ML)))
print('MR: {:>7.03f} < {:> 4.03f}'.format(*cmath.polar(MR)))
