#!/opt/software/anaconda/python-3.10.9/bin/python

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
   
    
   #VECTOR OPERATIONS
    
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
        
       return vector((self2.xval * self.xval) +
                     (self2.yval * self.yval) +
                     (self2.zval * self.zval))
    
   def vectorproduct(self, self2):
       
       xvp = self.yval * self2.zval - self.zval * self2.yval
       yvp = self.zval * self2.xval - self.xval * self2.zval
       zvp = self.xval * self2.yval - self.yval * self2.xval
       
       return vector(xvp, yvp, zvp)

#test vector
v1 = vector(3, 5, 6)

print(f"Vector Coords are: {v1.xval, v1.yval, v1.zval}") 
print(f"Vector is of magnitude: {v1.magnitude():.3f}")

ux1, uy1, uz1 = v1.unitvectors()
print(f"Unit Vectors are (x, y, z): {ux1, uy1, uz1}")

alpha1, beta1, gamma1 = v1.direction()
print(f"Vector is of direction (alpha, beta, gamma): {alpha1, beta1, gamma1} degrees")

#VECTOR OPERATIONS (ADDITION, SUBTRACTION, DOT/SCALAR PRODUCT)

dimensions = 3

def create_vector(dimensions):
    return [np.random.randint(0, 100) for x in range(dimensions)]

v2 = vector(*create_vector(dimensions))
v3 = vector(*create_vector(dimensions)) 

print(f"Vector 2 properties: {v2.xval, v2.yval, v2.zval} of magnitude {v2.magnitude():.3f}") 
print(f"Vector 3 properties: {v3.xval, v3.yval, v3.zval} of magnitude {v3.magnitude():.3f}")

vadd32 = v2.addition(v3)
vsub32 = v2.subtraction(v3)
vsp32 = v2.scalarproduct(v3)
vvp32 = v2.vectorproduct(v3)

print(f'Addition = {vadd32.xval, vadd32.yval, vadd32.zval}')
print(f'Subtraction = {vsub32.xval, vsub32.yval, vsub32.zval}')
print(f'Scalar Product = {vsp32}')
print(f'Vector product = {vvp32.xval, vvp32.yval, vvp32.zval}')
