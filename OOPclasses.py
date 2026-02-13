#!/opt/software/anaconda/python-3.10.9/bin/python

"""
Version: Python 3.10.9

Description: Using OOP classes to represent and manipulate cartesian vectors.

Date: 12/02/2026

Author: Nicholas Young
"""

iimport math
import numpy as np


class vector:
   type = 'Vector'

   def __init__(self, xval, yval, zval):
       
       self.xval = xval
       self.yval = yval
       self.zval = zval
       
   def magnitude(self):

      mag = np.sqrt((self.xval*self.xval) + (self.yval*self.yval) + (self.zval*self.zval))
      
      return mag
  
   def unitvectors(self):
       
       mag = self.magnitude()
       
       return (self.xval / mag, self.yval / mag, self.zval / mag)
    
   def direction(self):
       
       ux, uy, uz = self.unitvectors()
       
       alpha = math.degrees(math.acos(ux))
       beta = math.degrees(math.acos(uy))
       gamma = math.degrees(math.acos(uz))
       
       return alpha, beta, gamma

v1 = vector(3, 5, 6)

print(f"Vector Coords are: {v1.xval, v1.yval, v1.zval}") 
print(f"Vector is of magnitude: {v1.magnitude():.3f}")

ux1, uy1, uz1 = v1.unitvectors()
print(f"Unit Vectors are (x, y, z): {ux1, uy1, uz1}")

alpha1, beta1, gamma1 = v1.direction()
print(f"Vector is of direction: {alpha1, beta1, gamma1} degrees")
