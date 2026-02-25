#!/opt/software/anaconda/python-3.10.9/bin/python

# =============================================================================
# MIT License
#
# Copyright (c) 2026 Nicholas Young
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================

"""
Version: Python 3.10.9

Description: Using OOP classes to represent and manipulate real and complex 3D cartesian vectors.

Date: 24/02/2026

Author: Nicholas Young
"""

import math
import numpy as np # pylint: disable=import-error

# CREATING VECTOR CLASS

class Vector:

    """
    Class representing a 3D vector (x,y,z) of direction and magnitude.
    This class also features core vector operations, such as addition,
    subtraction, scalar and vector products.

    Features:
    """

    type = "Vector"

    # VECTOR TRAITS

    def __init__(self, xval, yval, zval):

        "x, y and z real components of the 3D vector."

        self.xval = xval
        self.yval = yval
        self.zval = zval

    def magnitude(self):

        "Magnitude of the vector from provided real components."

        return np.sqrt(
            np.abs(self.xval*self.xval) +
            np.abs(self.yval*self.yval) +
            np.abs(self.zval*self.zval))

    def unitvectors(self):

        "Unit vectors x,y and z calculated the vector magnitude and its components."

        mag = self.magnitude()

        return (self.xval / mag, self.yval / mag, self.zval / mag)

    def direction(self):

        "From the x, y and z unit vectors we can derive the angles of direction in degrees."

        ux, uy, uz = self.unitvectors()

        alpha = math.degrees(math.acos(ux))
        beta = math.degrees(math.acos(uy))
        gamma = math.degrees(math.acos(uz))

        return alpha, beta, gamma

    # BASIC VECTOR OPERATIONS

    def __add__(self, other):

        "Vector addition for two vectors of real components x,y and z."

        return Vector(
            self.xval + other.xval,
            self.yval + other.yval,
            self.zval + other.zval
            )

    def __sub__(self, other):

        "Vector subtraction for two vectors of real components x,y and z."

        return Vector(
        self.xval - other.xval,
        self.yval - other.yval,
        self.zval - other.zval
        )

    def __mul__(self, other):

        "Multiplication of a scalar with a vector."

        return Vector(self.xval * other, self.yval * other, self.zval * other)

    def __rmul__(self, other):

        "Multiplication of a scalar with a vector reversed."

        return self.__mul__(other)

    def __truediv__(self, other):

        "Division of a vector components by a scalar."

        return Vector(self.xval / other, self.yval / other, self.zval / other)

    # PRODUCTS

    def scalarproduct(self, self2):

        "Scalar product for two vectors of real components x,y and z"

        return (self2.xval * self.xval) + (self2.yval * self.yval) + (self2.zval * self.zval)

    def vectorproduct(self, self2):

        "Vector product for two vectors of components x, y and z"

        xvp = self.yval * self2.zval - self.zval * self2.yval
        yvp = self.zval * self2.xval - self.xval * self2.zval
        zvp = self.xval * self2.yval - self.yval * self2.xval

        return Vector(xvp, yvp, zvp)

    def productmagnitude(self, self2):

        "Calculates the magnitude of of a vector connecting two points of components x, y and z"

        xvp = self.yval * self2.zval - self.zval * self2.yval
        yvp = self.zval * self2.xval - self.xval * self2.zval
        zvp = self.xval * self2.yval - self.yval * self2.xval

        return np.sqrt(xvp*xvp + yvp*yvp + zvp*zvp)

    def productdirection(self, self2):

        "The direction of a vector connecting two points of components x, y and z"

        mag1 = self.magnitude()
        mag2 = self2.magnitude()

        xvp = self.yval * self2.zval - self.zval * self2.yval
        yvp = self.zval * self2.xval - self.xval * self2.zval
        zvp = self.xval * self2.yval - self.yval * self2.xval

        vpmag = np.sqrt(xvp*xvp + yvp*yvp + zvp*zvp)

        return math.degrees(math.asin(vpmag / (mag1 * mag2)))

#test vector to see if class works

print('')
print('TESTING VECTOR PROPERTIES (COMPONENTS, MAGNITUDE, UNITS AND DIRECTION ANGLES)')
print('')

v1test = Vector(3, 5, 6)

print(f'Vector Components are: {v1test.xval, v1test.yval, v1test.zval}')
print(f'Vector is of magnitude: {v1test.magnitude():.3f}')

ux1, uy1, uz1 = v1test.unitvectors()
print(f'Unit Vectors are (x, y, z): {ux1, uy1, uz1}')

alpha1, beta1, gamma1 = v1test.direction()
print('Vector is of direction (alpha, beta, gamma):',
     f'{alpha1:.2f}, {beta1:.2f}, {gamma1:.2f} degrees')
print('')

###############################################################################
################################### TASK1 #####################################
###############################################################################
# VECTOR OPERATIONS (ADDITION, SUBTRACTION, DOT/CROSS PRODUCT)

print('#################### TASK 1 TEST ####################')

def create_vector(d = 3):

    """
    Generates a 3D vector of random x,y and z components
    between a value of -50 and 50
    """

    return [np.random.randint(-50, 50) for x in range(d)]

print('')
print('VECTOR PROPERTIES')
print('')

# TWO RANDOMLY GENERATED VECTORS TO USE FOR OPERATIONS

v2 = Vector(*create_vector(3))
v3 = Vector(*create_vector(3))

print('Vector 2 components and magnitude:',
     f'{v2.xval, v2.yval, v2.zval} of magnitude {v2.magnitude():.3f}')
print('Vector 3 components and magnitude:'
     f'{v3.xval, v3.yval, v3.zval} of magnitude {v3.magnitude():.3f}')

print('')
print('VECTOR OPERATIONS')
print('')

vadd32 = v2 + v3
vsub32 = v3 - v2
vsp32 = v2.scalarproduct(v3)
vvp32 = v2.vectorproduct(v3)
vvpm32 = v2.productmagnitude(v3)
vvpd32 = v2.productdirection(v3)

print(f'Addition = {vadd32.xval, vadd32.yval, vadd32.zval}')
print(f'Subtraction = {vsub32.xval, vsub32.yval, vsub32.zval}')
print(f'Scalar Product = {vsp32:.2f}')
print(f'Vector product = {vvp32.xval, vvp32.yval, vvp32.zval}')
print(f'Vector product magnitude = {vvpm32:.2f}')
print(f'Vector product direction = {vvpd32:.2f} degrees')
print('')

###############################################################################
################################### TASK2 #####################################
###############################################################################

print('#################### TASK 2 RESULTS ####################')
print('')

########## TRIANGLE 1 ###########

# CREATE VECTORS FROM TRIANGLE COORDINATES
tri1A = Vector(0,0,0)
tri1B = Vector(1,0,0)
tri1C = Vector(0,1,0)

# USE VECTOR GEOMETRY FOR AREA. A = MAGNITUDE (B-A x C-A) * 0.5
tri1AB = tri1B - tri1A
tri1AC = tri1C - tri1A

area1 = tri1AB.productmagnitude(tri1AC) * 0.5

print(f'Triangle 1 area = {area1:.2f}')

# FIND COMPONENTS OF VECTORS CONNECTING THE TRIANGLES
tri1AB = tri1B - tri1A
tri1BC = tri1C - tri1B
tri1CA = tri1A - tri1C

tri1angleB = tri1AB.productdirection(tri1BC)
tri1angleC = tri1BC.productdirection(tri1CA)
tri1angleA = tri1CA.productdirection(tri1AB)

# REPEAT PROCESS FOR OTHER TRIANGLES
print(f'Triangle 1 angles A,B,C = {tri1angleA:.2f}, {tri1angleB:.2f}, {tri1angleC:.2f} degrees')
print('')

########## TRIANGLE 2 ###########

tri2A = Vector(-1,-1,-1)
tri2B = Vector(0,-1,-1)
tri2C = Vector(-1,0,-1)

tri2AB = tri2B - tri2A
tri2AC = tri2C - tri2A

area2 = tri2AB.productmagnitude(tri2AC) * 0.5

print(f'Triangle 2 area = {area2:.2f}')

tri2AB = tri2B - tri2A
tri2BC = tri2C - tri2B
tri2CA = tri2A - tri2C

tri2angleB = tri2AB.productdirection(tri2BC)
tri2angleC = tri2BC.productdirection(tri2CA)
tri2angleA = tri2CA.productdirection(tri2AB)

print(f'Triangle 2 angles A,B,C = {tri2angleA:.2f}, {tri2angleB:.2f}, {tri2angleC:.2f} degrees')
print('')

########## TRIANGLE 3 ###########

tri3A = Vector(1,0,0)
tri3B = Vector(0,0,1)
tri3C = Vector(0,0,0)

tri3AB = tri3B - tri3A
tri3AC = tri3C - tri3A

area3 = tri3AB.productmagnitude(tri3AC) * 0.5

print(f'Triangle 3 area = {area3:.2f}')

tri3AB = tri3B - tri3A
tri3BC = tri3C - tri3B
tri3CA = tri3A - tri3C

tri3angleB = tri3AB.productdirection(tri3BC)
tri3angleC = tri3BC.productdirection(tri3CA)
tri3angleA = tri3CA.productdirection(tri3AB)

print(f'Triangle 3 angles A,B,C = {tri3angleA:.2f}, {tri3angleB:.2f}, {tri3angleC:.2f} degrees')
print('')

########## TRIANGLE 4 ###########

tri4A = Vector(0,0,0)
tri4B = Vector(1,-1,0)
tri4C = Vector(0,0,1)

tri4AB = tri4B - tri4A
tri4AC = tri4C - tri4A

area4 = tri4AB.productmagnitude(tri4AC) * 0.5

print(f'Triangle 4 area = {area4:.2f}')

tri4AB = tri4B - tri4A
tri4BC = tri4C - tri4B
tri4CA = tri4A - tri4C

tri4angleB = tri4AB.productdirection(tri4BC)
tri4angleC = tri4BC.productdirection(tri4CA)
tri4angleA = tri4CA.productdirection(tri4AB)

print(f'Triangle 4 angles A,B,C = {tri4angleA:.2f}, {tri4angleB:.2f}, {tri4angleC:.2f} degrees')
print('')

###############################################################################
################################### TASK3 #####################################
###############################################################################
#CURL AND DIVERGENCE OF HANSEN VECTORS.

print('#################### TASK 3 RESULTS ####################')
print('')

def cxprint(cnum, ndp=2):

    "Function to cleanly print complex numbers to defined decimal place"

    sign = '+' if cnum.imag >= 0 else '-'
    return f'{cnum.real:.{ndp}f} {sign} {abs(cnum.imag):.{ndp}f}j'

def vecprint(vec, ndp=2):

    "Function to cleanly print complex vector components to a defined decimal place"

    return f'({cxprint(vec.xval, ndp)}, {cxprint(vec.yval, ndp)}, {cxprint(vec.zval, ndp)})'

# BUILD A COMPLEX VECTOR SUBCLASS WHICH DIRECTLY INHERITS FUNCTIONS FROM THE VECTOR CLASS
class ComplexVector(Vector):

    """
    A class to represent complex 3D vectors, it directly inherits
    functions from the vector class. The divergence and curl are
    calculated through the central finite difference formula.
    """

    type: 'ComplexVector'

    def conjugate(self):

        "Calculates the complex conjugate of a complex vector of components x, y and z."

        return ComplexVector(np.conj(self.xval), np.conj(self.yval), np.conj(self.zval))

    def cscalarproduct(self, self2):

        "Scalar product of two complex vectors of components x, y and z"

        return (np.conj(self.xval)*self2.xval +
                np.conj(self.yval)*self2.yval +
                np.conj(self.zval)*self2.zval)

    # WHILE CURL AND DIVERGENCE DON'T REQUIRE SELF IT FELT CLEANER TO STORE THEM INSIDE THE CLASS.
    # THE APPROXIMATION HERE USES VARIBALE 'h'.
    # THIS VALUE MUST BE KEPT AROUND 1E-6 TO MAINTAIN ACCURACY.

    @staticmethod
    def divergence(f, x, y, z, h = 1e-6):

        """
        Divergence of a 3 variable function (x, y, z) using
        the central finite difference approximation.
        """

        fx_max = f(x+h, y, z).xval
        fx_min = f(x-h, y, z).xval
        dfxdx = (fx_max - fx_min) / (2*h)

        fy_max = f(x, y+h, z).yval
        fy_min = f(x, y-h, z).yval
        dfydy = (fy_max - fy_min) / (2*h)

        fz_max = f(x, y, z+h).zval
        fz_min = f(x, y, z-h).zval
        dfzdz = (fz_max - fz_min) / (2*h)

        return dfxdx + dfydy + dfzdz

    @staticmethod
    def curl(f, x, y, z, h = 1e-6):

        """
        Curl of a 3 variable function (x, y, z) using
        the central finite difference approximation.
        """

        dfzdy = (f(x, y+h, z).zval - f(x, y-h, z).zval) / (2*h)

        dfydz = (f(x, y, z+h).yval - f(x, y, z-h).yval) / (2*h)

        dfxdz = (f(x, y, z+h).xval - f(x, y, z-h).xval) / (2*h)

        dfzdx = (f(x+h, y, z).zval - f(x-h, y, z).zval) / (2*h)

        dfydx = (f(x+h, y, z).yval - f(x-h, y, z).yval) / (2*h)

        dfxdy = (f(x, y+h, z).xval - f(x, y-h, z).xval) / (2*h)

        return ComplexVector(dfzdy - dfydz,
                              dfxdz - dfzdx,
                              dfydx - dfxdy)

# HANSEN VECTORS 'M' AND 'N'

def hansen_n(_xm, _ym, zm):

    """
    M Hansen Vector for a plane-polarized electromagnetic wave
    propagating in vacuum.
    """

    phase = np.exp(1j * np.pi * zm)

    return ComplexVector(phase, 0.0 + 0.0j, 0.0 + 0.0j)

def hansen_m(_xn, _yn, zn):

    """
    N Hansen Vector for a plane-polarized electromagnetic wave
    propagating in vacuum.
    """

    phase = np.exp(1j * np.pi * zn)

    return ComplexVector(0.0 + 0.0j, phase, 0.0 + 0.0j)

# POINTS TO TEST HANSEN VECTORS.
# x and y are kept at 0 here as z is the only relevant component in these calculations.
points = [
    (0.0, 0.0, 0.0),
    (0.0, 0.0, 0.5),
    (0.0, 0.0, 1.0),
    (0.0, 0.0, -1.0),
    (0.0, 0.0, 36.8)]

# MAGNITUDE OF VECTOR K = (0, 0, PI)
k_mag = np.pi

print('########## BEGIN EVALUATING FOR DIFFERENT Z VALUES ##########')
print('(NumPy version)')

# VALUES TO COMPARE WITH SYMPY CALCULATIONS

for (xp, yp, zp) in points:

    print(f'########## Points = ({xp},{yp},{zp}) ##########')
    print('')

    M = hansen_m(xp, yp, zp)
    N = hansen_n(xp, yp, zp)

    print('Hansen Vector M =', vecprint(M))
    print('Hansen Vector N =', vecprint(N))
    print('')

    divM = ComplexVector.divergence(hansen_m, xp, yp, zp)
    divN = ComplexVector.divergence(hansen_n, xp, yp, zp)

    print('Divergence of M =', cxprint(divM))
    print('Divergence of N =', cxprint(divN))
    print('')

    curlM = ComplexVector.curl(hansen_m, xp, yp, zp)
    curlN = ComplexVector.curl(hansen_n, xp, yp, zp)

    print('Curl of M =', vecprint(curlM))
    print('Curl of N =', vecprint(curlN))
    print('')

    M_kmag_div = ComplexVector(M.xval/k_mag, M.yval/k_mag, M.zval/k_mag)
    N_kmag_div = ComplexVector(N.xval/k_mag, N.yval/k_mag, N.zval/k_mag)

    print('M/mag(k) =', vecprint(M_kmag_div))
    print('N/mag(k) =', vecprint(N_kmag_div))
    print('')

    falseMproof = M_kmag_div - curlN
    falseNproof = N_kmag_div - curlM

    print('M/mag(k) - curl(N)', vecprint(falseMproof))
    print('N/mag(k) - curl(M)', vecprint(falseNproof))
    print('')

    # In the assignment notes it says this should be equal but it isn't. This rule is incorrect.
    # Below we solve the correct expression by working backwards from the previous result.

    M_kmag_times = ComplexVector(M.xval*k_mag*-1j, M.yval*k_mag*-1j, M.zval*k_mag*-1j)
    N_kmag_times = ComplexVector(N.xval*k_mag*1j, N.yval*k_mag*1j, N.zval*k_mag*1j)

    print('M*mag(k) =', vecprint(M_kmag_times))
    print('N*mag(k) =', vecprint(N_kmag_times))
    print('')

    trueMproof = M_kmag_times - curlN
    trueNproof = N_kmag_times - curlM

    print('M*mag(k) - curl(N)', vecprint(trueMproof))
    print('N*mag(k) - curl(M)', vecprint(trueNproof))
    print('')
