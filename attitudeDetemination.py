# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 09:31:55 2022

@author: Malachi
"""

""" Dependencies"""
import numpy as np


#inputs
#measurements in body frame
v1B_x = 2
v1B_y = 1
v1B_z = 0

v2B_x = 1
v2B_y = 0
v2B_z = 0

#truth states in inertial frame
v1I_x = 0
v1I_y = 1
v1I_z = 0

v2I_x = 1
v2I_y = 0
v2I_z = 0


#place in vectors - these all need to be unit length eventually
#body frame measurements
v1b = [v1B_x, v1B_y, v1B_z]
v2b = [v2B_x, v2B_y, v2B_z]

#inertial frame state
v1i = [v1I_x, v1I_y, v1I_z]
v2i = [v2I_x, v2I_y, v2I_z]



#Construction of TRIAD in body coord frame
#take v1 to be our most accurate measurement
t1_b = v1b

t2_b = np.cross(v1b,v2b)
t2_b = t2_b / np.linalg.norm(t2_b)

t3_b = np.cross(t1_b, t2_b)

t_b = np.array([t1_b, t2_b, t3_b])

#Construction of TRIAD in inertial frame
t1_i = v1i

t2_i = np.cross(v1i,v2i)
t2_i = t2_i / np.linalg.norm(t2_i)

t3_i = np.cross(t1_i, t2_i)

t_i = np.array([t1_i, t2_i, t3_i])

#Compute rotation matrix between triads
R = np.matmul(t_b,t_i.transpose())






