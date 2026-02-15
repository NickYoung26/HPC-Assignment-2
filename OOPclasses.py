#!/opt/software/anaconda/python-3.10.9/bin/python

"""
Version: Python 3.10.9

Description: Using OOP classes to represent and manipulate cartesian vectors.

Date: 12/02/2026

Author: Nicholas Young
"""

import math
import numpy as np

# CREATING VECTOR CLASS

class vector:
    
   type = 'Vector'
   
   # VECTOR TRAITS

   def __init__(self, xval, yval, zval):
       
       self.xval = xval
       self.yval = yval
       self.zval = zval
       
   def magnitude(self):

      return np.sqrt((self.xval*self.xval) + (self.yval*self.yval) + (self.zval*self.zval))
  
   def unitvectors(self):
       
       mag = self.magnitude()
       
       return (self.xval / mag, self.yval / mag, self.zval / mag)
    
   def direction(self):
       
       ux, uy, uz = self.unitvectors()
       
       alpha = math.degrees(math.acos(ux))
       beta = math.degrees(math.acos(uy))
       gamma = math.degrees(math.acos(uz))
       
       return alpha, beta, gamma
   
    
   # VECTOR OPERATIONS
    
   def addition(self, self2):
       
       xadd = self.xval + self2.xval
       yadd = self.yval + self2.yval
       zadd = self.zval + self2.zval
        
       return vector(xadd, yadd, zadd)
    
   def subtraction(self, self2):
       
       xsub = self2.xval - self.xval
       ysub = self2.yval - self.yval
       zsub = self2.zval - self.zval
       
       return vector(xsub, ysub, zsub)
    
   def scalarproduct(self, self2):
        
       return (self2.xval * self.xval) + (self2.yval * self.yval) + (self2.zval * self.zval)
    
   def vectorproduct(self, self2):
       
       xvp = self.yval * self2.zval - self.zval * self2.yval
       yvp = self.zval * self2.xval - self.xval * self2.zval
       zvp = self.xval * self2.yval - self.yval * self2.xval
       
       #np.cross(self, self2)?
       
       return vector(xvp, yvp, zvp)
   
   def productmagnitude(self, self2):
       
       xvp = self.yval * self2.zval - self.zval * self2.yval
       yvp = self.zval * self2.xval - self.xval * self2.zval
       zvp = self.xval * self2.yval - self.yval * self2.xval
       
       return np.sqrt(xvp*xvp + yvp*yvp + zvp*zvp)
   
   def productdirection(self, self2):
       
       mag1 = self.magnitude()
       mag2 = self2.magnitude()
       
       xvp = self.yval * self2.zval - self.zval * self2.yval
       yvp = self.zval * self2.xval - self.xval * self2.zval
       zvp = self.xval * self2.yval - self.yval * self2.xval
       
       vpmag = np.sqrt(xvp*xvp + yvp*yvp + zvp*zvp)
       
       return math.degrees(math.asin(vpmag / (mag1 * mag2)))

#test vector

print('')
print('TERSTING VECTOR PROPERTIES (COMPONENTS, MAGNITUDE, UNITS AND DIRECTION ANGLES)')
print('')

v1 = vector(3, 5, 6)

print(f"Vector Components are: {v1.xval, v1.yval, v1.zval}") 
print(f"Vector is of magnitude: {v1.magnitude():.3f}")

ux1, uy1, uz1 = v1.unitvectors()
print(f"Unit Vectors are (x, y, z): {ux1, uy1, uz1}")

alpha1, beta1, gamma1 = v1.direction()
print(f"Vector is of direction (alpha, beta, gamma): {alpha1:.2f}, {beta1:.2f}, {gamma1:.2f} degrees")
print('')

#TASK1
#VECTOR OPERATIONS (ADDITION, SUBTRACTION, DOT/SCALAR PRODUCT) 
print('#################### TASK 1 TEST ####################')

dimensions = 3

def create_vector(dimensions):
    return [np.random.randint(-50, 50) for x in range(dimensions)]

print('')
print('VECTOR PROPERTIES')
print('')

v2 = vector(*create_vector(dimensions))
v3 = vector(*create_vector(dimensions)) 

print(f"Vector 2 components and magnitude: {v2.xval, v2.yval, v2.zval} of magnitude {v2.magnitude():.3f}") 
print(f"Vector 3 components and magnitude: {v3.xval, v3.yval, v3.zval} of magnitude {v3.magnitude():.3f}")

print('')
print('VECTOR OPERATIONS')
print('')

vadd32 = v2.addition(v3)
vsub32 = v2.subtraction(v3)
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

#TASK2
#CREATE VECTORS FROM COORDINATES
print('#################### TASK 2 RESULTS ####################')
print('')
###############################################################################
################################### TRIANGLE 1 ################################
###############################################################################

tri1A = vector(0,0,0)
tri1B = vector(1,0,0)
tri1C = vector(0,1,0)

tri1BA = tri1A.subtraction(tri1B)
tri1CA = tri1A.subtraction(tri1C) 

area1 = tri1BA.productmagnitude(tri1CA)

print(f'Triangle 1 area = {area1:.2f}')

tri1AB = tri1A.subtraction(tri1B)
tri1BC = tri1B.subtraction(tri1C)
tri1CA = tri1C.subtraction(tri1A)

tri1angleB = tri1AB.productdirection(tri1BC)
tri1angleC = tri1BC.productdirection(tri1CA)
tri1angleA = tri1CA.productdirection(tri1AB)

print(f'Triangle 1 angles A,B,C = {tri1angleA:.2f}, {tri1angleB:.2f}, {tri1angleC:.2f} degrees')
print('')

###############################################################################
################################### TRIANGLE 2 ################################
###############################################################################

tri2A = vector(-1,-1,-1)
tri2B = vector(0,-1,-1)
tri2C = vector(-1,0,-1)

tri2BA = tri2A.subtraction(tri2B)
tri2CA = tri2A.subtraction(tri2C) 

area2 = tri2BA.productmagnitude(tri2CA)

print(f'Triangle 2 area = {area2:.2f}')

tri2AB = tri2A.subtraction(tri2B)
tri2BC = tri2B.subtraction(tri2C)
tri2CA = tri2C.subtraction(tri2A)

tri2angleB = tri2AB.productdirection(tri2BC)
tri2angleC = tri2BC.productdirection(tri2CA)
tri2angleA = tri2CA.productdirection(tri2AB)

print(f'Triangle 2 angles A,B,C = {tri2angleA:.2f}, {tri2angleB:.2f}, {tri2angleC:.2f} degrees')
print('')

###############################################################################
################################### TRIANGLE 3 ################################
###############################################################################

tri3A = vector(1,0,0)
tri3B = vector(0,0,1)
tri3C = vector(0,0,0)

tri3BA = tri3A.subtraction(tri3B)
tri3CA = tri3A.subtraction(tri3C) 

area3 = tri3BA.productmagnitude(tri3CA)

print(f'Triangle 3 area = {area3:.2f}')

tri3AB = tri3A.subtraction(tri3B)
tri3BC = tri3B.subtraction(tri3C)
tri3CA = tri3C.subtraction(tri3A)

tri3angleB = tri3AB.productdirection(tri3BC)
tri3angleC = tri3BC.productdirection(tri3CA)
tri3angleA = tri3CA.productdirection(tri3AB)

print(f'Triangle 3 angles A,B,C = {tri3angleA:.2f}, {tri3angleB:.2f}, {tri3angleC:.2f} degrees')
print('')

###############################################################################
################################### TRIANGLE 4 ################################
###############################################################################

tri4A = vector(0,0,0)
tri4B = vector(1,-1,0)
tri4C = vector(0,0,1)

tri4BA = tri4A.subtraction(tri4B)
tri4CA = tri4A.subtraction(tri4C) 

area4 = tri4BA.productmagnitude(tri4CA)

print(f'Triangle 4 area = {area4:.2f}')

tri4AB = tri4A.subtraction(tri4B)
tri4BC = tri4B.subtraction(tri4C)
tri4CA = tri4C.subtraction(tri4A)

tri4angleB = tri4AB.productdirection(tri4BC)
tri4angleC = tri4BC.productdirection(tri4CA)
tri4angleA = tri4CA.productdirection(tri4AB)

print(f'Triangle 4 angles A,B,C = {tri4angleA:.2f}, {tri4angleB:.2f}, {tri4angleC:.2f} degrees')

#TASK 3


