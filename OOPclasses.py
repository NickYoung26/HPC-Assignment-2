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

###############################################################################
################################### TASK1 #####################################
###############################################################################
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

###############################################################################
################################### TASK2 #####################################
###############################################################################
#CREATE VECTORS FROM COORDINATES

print('#################### TASK 2 RESULTS ####################')
print('')


########## TRIANGLE 1 ###########


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

########## TRIANGLE 2 ###########

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

########## TRIANGLE 3 ###########

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

########## TRIANGLE 4 ###########

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

###############################################################################
################################### TASK3 #####################################
###############################################################################

#NICE FUNCTIONS TO NEATLY PRINT COMPLEX NUMBERS

print('#################### TASK 3 RESULTS ####################')
print('')

def cplexprint(z, ndp=2):
    sign = "+" if z.imag >= 0 else "-"
    return f"{z.real:.{ndp}f} {sign} {abs(z.imag):.{ndp}f}j"
    
def vecprint(V, ndp=2):
    return f"({cplexprint(V.xval, ndp)}, {cplexprint(V.yval, ndp)}, {cplexprint(V.zval, ndp)})"

class complexvector(vector):
    
    type: 'ComplexVector' 
    
    def conjugate(self):
        
        "Calculates the complex conjugate of a complex vector of components x, y and z."
        
        return complexvector(np.conj(self.xval), np.conj(self.yval), np.conj(self.zval))

    def cscalarproduct(self, self2):
        
        "Scalar product of two complex vectors of components x, y and z"
        
        return (np.conj(self.xval)*self2.xval +
                np.conj(self.yval)*self2.yval +
                np.conj(self.zval)*self2.zval)
    
    @staticmethod
    def divergence(F, x, y, z, h=1e-6):
        
        Fx_p = F(x+h, y, z).xval
        Fx_m = F(x-h, y, z).xval
        dFxdx = (Fx_p - Fx_m) / (2*h)

        Fy_p = F(x, y+h, z).yval
        Fy_m = F(x, y-h, z).yval
        dFydy = (Fy_p - Fy_m) / (2*h)

        Fz_p = F(x, y, z+h).zval
        Fz_m = F(x, y, z-h).zval
        dFzdz = (Fz_p - Fz_m) / (2*h)

        return dFxdx + dFydy + dFzdz
    
    @staticmethod
    def curl(F, x, y, z, h=1e-6):
        
        Fz_y_p = F(x, y+h, z).zval
        Fz_y_m = F(x, y-h, z).zval
        dFzdy = (Fz_y_p - Fz_y_m) / (2*h)

        Fy_z_p = F(x, y, z+h).yval
        Fy_z_m = F(x, y, z-h).yval
        dFydz = (Fy_z_p - Fy_z_m) / (2*h)

        Fx_z_p = F(x, y, z+h).xval
        Fx_z_m = F(x, y, z-h).xval
        dFxdz = (Fx_z_p - Fx_z_m) / (2*h)

        Fz_x_p = F(x+h, y, z).zval
        Fz_x_m = F(x-h, y, z).zval
        dFzdx = (Fz_x_p - Fz_x_m) / (2*h)

        Fy_x_p = F(x+h, y, z).yval
        Fy_x_m = F(x-h, y, z).yval
        dFydx = (Fy_x_p - Fy_x_m) / (2*h)

        Fx_y_p = F(x, y+h, z).xval
        Fx_y_m = F(x, y-h, z).xval
        dFxdy = (Fx_y_p - Fx_y_m) / (2*h)

        return complexvector(dFzdy - dFydz,
                              dFxdz - dFzdx,
                              dFydx - dFxdy)
   
# HANSEN VECTORS

def hansen_M(x, y, z):
    
    phase = np.exp(1j * np.pi * z)
    return complexvector(phase, 0.0 + 0.0j, 0.0 + 0.0j)

def hansen_N(x, y, z):
    phase = np.exp(1j * np.pi * z)
    return complexvector(0.0 + 0.0j, phase, 0.0 + 0.0j)

points = [
    (1.0, 1.0, 1.0),
    (0.0, 0.0, 0.0)]

k_mag = np.pi

for (x, y, z) in points:
    
    print(f'\nPoint (x,y,z) = ({x},{y},{z})')
    print('')
    
    M = hansen_M(x, y, z)
    N = hansen_N(x, y, z)
    
    print('M =', vecprint(M))
    print('N =', vecprint(N))
    print('')

    divM = complexvector.divergence(hansen_M, x, y, z)
    divN = complexvector.divergence(hansen_N, x, y, z)

    print('Divergence M =', cplexprint(divM))
    print('Divergence N =', cplexprint(divN))
    print('')

    curlM = complexvector.curl(hansen_M, x, y, z)
    curlN = complexvector.curl(hansen_N, x, y, z)
    
    print('Curl M =', vecprint(curlM))
    print('Curl N =', vecprint(curlN))
    print('')
    
    M_kmag_div = complexvector(M.xval/k_mag, M.yval/k_mag, M.zval/k_mag)
    N_kmag_div = complexvector(N.xval/k_mag, N.yval/k_mag, N.zval/k_mag)
    
    print('M/mag(k) =', vecprint(M_kmag_div))
    print('N/mag(k) =', vecprint(N_kmag_div))
    print('')
    
    print('Proof of Lies')
    print('M/mag(k) - curl(N)', vecprint(M_kmag_div.subtraction(curlN)))
    print('N/mag(k) - curl(N)', vecprint(N_kmag_div.subtraction(curlM)))
    print('')
    
    M_kmag_times = complexvector(M.xval*k_mag*-1j, M.yval*k_mag*-1j, M.zval*k_mag*-1j)
    N_kmag_times = complexvector(N.xval*k_mag*1j, N.yval*k_mag*1j, N.zval*k_mag*1j)
    
    print('M*mag(k) =', vecprint(M_kmag_times))
    print('N*mag(k) =', vecprint(N_kmag_times))
    print('')
    
    print('Proof of Truth')
    print('M*mag(k) - curl(N)', vecprint(curlN.subtraction(M_kmag_times)))
    print('N*mag(k) - curl(N)', vecprint(curlM.subtraction(N_kmag_times)))
    print('')
     
    MN_dot = M.cscalarproduct(N)
    MN_cross = M.vectorproduct(N)
    MN_cross_mag = MN_cross.magnitude()
    
    print('Proof its not the vectors (True Orthognality)')
    print('MN Dot Product =', cplexprint(MN_dot))
    print('MN Vector Product =', vecprint(MN_cross))
    print('MN Vector Product Magnitude =', cplexprint(MN_cross_mag))
    print('')


