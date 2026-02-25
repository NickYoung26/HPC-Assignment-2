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

Description: Using Sympy to verify divergence and curls of complex vectors.
See file 'oopclasses.py for context'.

Date: 24/02/2026

Author: Nicholas Young
"""

import sympy as sp

# AS M AND N DIVIDED BY MAG(K) DOES NOT EQUAL WHAT EXPECTED BY
# ASSINGMENT THIS TASK IS REPEATED USING SYMPY TO VERIFY
# OUR DIVERGENCE, CURL AND OTHER CALCULATIONS/PROOFS ARE ACCURATE.

# BEGIN TASK 3 SYMPY VERIFICATION

# CLEAN PRINTING FUNCTIONS

def cxprintsym(cnumsym, ndp=2):

    "Function to cleanly print SymPy complex numbers to a defined decimal place"

    expr = sp.simplify(cnumsym)

    # If it still has symbols, don't try to convert to float/complex
    if expr.free_symbols:
        return str(expr)

    # Otherwise it's numeric so format as before
    val = complex(sp.N(expr, ndp + 5))
    sign = "+" if val.imag >= 0 else "-"
    return f"{val.real:.{ndp}f} {sign} {abs(val.imag):.{ndp}f}j"

def vecprintsym(symvec, ndp=2):

    "Function to cleanly print SymPy complex vector components to a defined decimal place"

    return f"({cxprintsym(symvec.x, ndp)},{cxprintsym(symvec.y, ndp)},{cxprintsym(symvec.z, ndp)})"

# NOTE -  NO CLASS INHERITANCE HERE AS WE ARE USING A DIFFERENT PACKAGE FOR
# CALCULATIONS (SymPy).
# THIS WORK MERELY ACTS A PROOF OF PREVIOUS WORK IN TASK 3 FROM FILE
# 'oopclasses.py'

class ComplexVectorSym:

    """
    A complex vector class using SymPy. Allowing for accurate algebraic and product calculations
    """

    def __init__(self, x, y, z):

        "Initialiser of complex vector components x, y and z."

        self.x = sp.sympify(x)
        self.y = sp.sympify(y)
        self.z = sp.sympify(z)

    # CORE OPERATIONS

    def __add__(self, other):

        "Vector addition for two vectors of complex components x,y and z."

        return ComplexVectorSym(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
            )

    def __sub__(self, other):

        "Vector subtraction for two vectors of complex components x,y and z."

        return ComplexVectorSym(
        self.x - other.x,
        self.y - other.y,
        self.z - other.z
        )

    def __mul__(self, other):

        "Multiplication of a scalar with a matrix."

        return ComplexVectorSym(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):

        "Multiplication of a scalar with a matrix reversed."

        return self.__mul__(other)

    def __truediv__(self, other):

        "Division of a matrices components by a scalar."

        return ComplexVectorSym(self.x / other, self.y / other, self.z / other)

    def evalf(self):

        "Converts SymPy expressions to decimal numbers e.g(pi)"

        return ComplexVectorSym(sp.N(self.x), sp.N(self.y), sp.N(self.z))

    # PRODUCTS

    def cdot(self, other):

        "Scalar product of two complex vectors of components x, y and z"

        return sp.simplify(
            sp.conjugate(self.x)*other.x +
            sp.conjugate(self.y)*other.y +
            sp.conjugate(self.z)*other.z)

    def cross(self, other):

        "Vector product of two complex vectors of components x, y and z"

        cxcross = sp.simplify(self.y*other.z - self.z*other.y)
        cycross = sp.simplify(self.z*other.x - self.x*other.z)
        czcross = sp.simplify(self.x*other.y - self.y*other.x)

        return ComplexVectorSym(cxcross, cycross, czcross)

    def div(self, x, y, z):

        "Divergence of a 3D vector of components (x, y, z)."

        return sp.simplify(
            sp.diff(self.x, x) +
            sp.diff(self.y, y) +
            sp.diff(self.z, z))

    def curl(self, x, y, z):

        "Curl of a 3D vector of compoennts (x, y, z)."

        xcurl = sp.simplify(sp.diff(self.z, y) - sp.diff(self.y, z))
        ycurl = sp.simplify(sp.diff(self.x, z) - sp.diff(self.z, x))
        zcurl = sp.simplify(sp.diff(self.y, x) - sp.diff(self.x, y))

        return ComplexVectorSym(xcurl, ycurl, zcurl)

    def conjugate(self):

        "Calculates the complex conjugate of a complex vector of components x, y and z."

        conjx = sp.conjugate(self.x)
        conjy = sp.conjugate(self.y)
        conjz = sp.conjugate(self.z)

        return ComplexVectorSym(conjx, conjy, conjz)

    def subs(self, symbol, value):

        "Used to sub in values of z to matrices for operations"

        return ComplexVectorSym(
        self.x.subs(symbol, value),
        self.y.subs(symbol, value),
        self.z.subs(symbol, value)
    )

# DEFINING HANSEN VECTORS

x, y, z = sp.symbols('x y z', real=True)
k = sp.pi
symphase = sp.exp(sp.I * k * z)

M = ComplexVectorSym(symphase, 0, 0)
N = ComplexVectorSym(0, symphase, 0)

print('########## HANSEN VECTORS AND PRODUCT EXPRESSIONS ##########')
print('(SymPy Version)')
print('')

print('Hansen M =', vecprintsym(M))
print('Hansen N =', vecprintsym(N))
print('')

MdotN = M.cdot(N)
McrossN = M.cross(N)

print('M.N =', MdotN)
print('M×N =', vecprintsym(McrossN))

print('')

# DERIVE ALGEBRAIC EXPRESSIONS TO EVALUATE FOR POINTS OF Z.

divM_expr = M.div(x, y, z)
divN_expr = N.div(x, y, z)

print('div M =', cxprintsym(divM_expr))
print('div N =', cxprintsym(divM_expr))
print('')

curlM_expr = M.curl(x, y, z)
curlN_expr = N.curl(x, y, z)

print('curl M =', vecprintsym(curlM_expr))
print('curl N =', vecprintsym(curlN_expr))
print('')

kmag = sp.pi

# INCORRECT RULE
M_over_k_expr = M / kmag
N_over_k_expr = N / kmag

print('M/mag(k) =', vecprintsym(M_over_k_expr))
print('N/mag(k) =', vecprintsym(N_over_k_expr))
print('')

# CORRECT RULE
M_times_k_expr = -kmag * sp.I * M
N_times_k_expr = kmag * sp.I * N

print('M*mag(k) =', vecprintsym(M_times_k_expr))
print('N*mag(k) =', vecprintsym(N_times_k_expr))
print('')

print('########## BEGIN EVALUATING FOR DIFFERENT Z VALUES ##########')
print('(SymPy Version)')
print('')

# Z VALUES TO BE CALCULATED.
z_values = [0, 1, -1, 36.8]

for z0 in (z_values):

    print(f"########## At z = {z0} ##########")
    print('')

    M_val = M.subs(z, z0)
    N_val = N.subs(z, z0)

    print('M = ', vecprintsym(M_val))
    print('N = ', vecprintsym(N_val))
    print('')

    divM_val = divM_expr.subs(z, z0)
    divN_val = divN_expr.subs(z, z0)

    print('div M =', cxprintsym(sp.N(divM_val)))
    print('div N =', cxprintsym(sp.N(divN_val)))
    print('')

    curlM_val = curlM_expr.subs(z, z0)
    curlN_val = curlN_expr.subs(z, z0)

    print('curl M =', vecprintsym(curlM_val.evalf()))
    print('curl N =', vecprintsym(curlN_val.evalf()))
    print('')

    M_valfalse = M_over_k_expr.subs(z, z0).evalf()
    N_valfalse = N_over_k_expr.subs(z, z0).evalf()

    print('M/mag(k) =', vecprintsym(M_valfalse, 2))
    print('N/mag(k) =', vecprintsym(N_valfalse, 2))
    print('')

    falseMproofsym = M_valfalse - curlN_val
    falseNproofsym = N_valfalse - curlM_val

    print('M/mag(k) - curl(N) =', vecprintsym(falseMproofsym))
    print('N/mag(k) - curl(M) =', vecprintsym(falseNproofsym))
    print('')

    M_valtrue = M_times_k_expr.subs(z, z0).evalf()
    N_valtrue = N_times_k_expr.subs(z, z0).evalf()

    print('M*mag(k) =', vecprintsym(M_valtrue, 2))
    print('N*mag(k) =', vecprintsym(N_valtrue, 2))
    print('')

    trueMproofsym = M_valtrue - curlN_val
    trueNproofsym = N_valtrue - curlM_val

    print('M*mag(k) - curl(N) =', vecprintsym(trueMproofsym))
    print('N*mag(k) - curl(N) =', vecprintsym(trueNproofsym))
    print('')
