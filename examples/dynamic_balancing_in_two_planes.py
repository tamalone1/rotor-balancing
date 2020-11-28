# -*- coding: utf-8 -*-
"""

Copyright (c) 2020 tamalone1
"""
import cmath
from math import radians
import rotor_balancing

# Baseline reactions (length)
XA = cmath.rect(8.6, radians(63))
XB = cmath.rect(6.5, radians(206))
# Trial masses and locations (mg-m) on planes L and R respectively
mL = cmath.rect(10, radians(270))
mR = cmath.rect(12, radians(180))
# Trial reactions using mL on plane L (length)
XAL = cmath.rect(5.9, radians(123))
XBL = cmath.rect(4.5, radians(228))
# Trial reactions using mR on plane R (length)
XAR = cmath.rect(6.2, radians(36))
XBR = cmath.rect(10.4, radians(162))
# Stiffness = change in the bearing reaction divided by the trial mass that
# caused it. One value per bearing per trial mass
left_stiffnesses = rotor_balancing.get_stiffnesses(XAL, XBL, XA, XB, mL)
right_stiffnesses = rotor_balancing.get_stiffnesses(XAR, XBR, XA, XB, mR)
# The existing unbalances and their locations, on planes L and R
ML, MR = rotor_balancing.required_balances(*left_stiffnesses, *right_stiffnesses, XA, XB)
# Print the result in polar form like the problem statement
print('ML: {:.03f} <{:4.03f}'.format(*cmath.polar(ML)))
print('MR: {:.03f} <{:4.03f}'.format(*cmath.polar(MR)))