# Rotor Balancing 

Balance rotating machine parts, such as shafts, rotors, and pulleys. Using input
data about the rotation speed and reaction speeds, determine where to attach or 
remove mass to bring the part into balance.

Background concepts:

In a rotating machine part, imbalance occurs when the mass is not distributed 
around the rotation avis perfectly. This causes unequal centrifugal forces on 
the part as it rotates. These net forces create extra loads on the bearings, 
cause vibration, and lead to premature fatigue failure.

---
## Installing

Requirements:
* No requirements outside the Python Standard Library

Install by cloning this repo and using `pip`:

```python
cd rotor-balancing
pip install -e rotor_balancing
```
Note the -e flag, which installs in editable mode and allows you to modify the
source at will after installing.
---
## Usage

Imbalances are dealt with in terms of mass x radius (kg-m). 

**balance_one_plane**: 

Determine the added balance mass needed to balance a single plane, based on the 
known imbalances in that plane. Known imbalances are given in vector form, in 
units of mass*radius. 

### Dynamic Balancing using test masses
To balance a given rotor, the existing imbalances have to be measured and 
located. This can be done by using the **dynamic_balance** method. Three test 
runs are required, measuring the deflection of the rotor bearings while rotating
with two test masses. Sensors should be set up to measure the bearing deflection
correlated with the angular position of the rotor. Choose two balance planes, 
locations where the added masses will be attached. Place a known test mass (kg-m)
on one plane, drive the rotor, and measure the deflection (magnitude and phase 
angle). Remove the test mass and repeat the process with a test mass (kg-m) in 
the other balance plane. Given the deflection magnitudes and phase angles at 
each bearing for each test mass (and the baseline), the method can determine the 
required balance masses to add to each balance plane to bring the rotor into 
dynamic balance.

---
## Contributing

Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the (insert license here) - see the [LICENSE.md](LICENSE.md) file for details

---
## References

* *Theory of Machines and Mechanisms, 4th ed*. Uicker, Pennock. 2010.

