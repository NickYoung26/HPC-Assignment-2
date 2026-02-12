#!/opt/software/anaconda/python-3.10.9/bin/python

"""
Version: Python 3.10.9

Description: Using OOP classes to represent and manipulate cartesian vectors.

Date: 12/02/2026

Author: Nicholas Young
"""

import math
import numpy as np


class vector:
   type = 'vector'

   def __init__(self, xval, yval, zval):

      self._xval = xval

      self._yval = yval

      self._zval = zval

   def magnitude(self):

      return np.abs(xval,yval,zval)

v1 = vector(3, 5, 6)

print(f"Vector is of magnitude: {v1.magnitude()})

