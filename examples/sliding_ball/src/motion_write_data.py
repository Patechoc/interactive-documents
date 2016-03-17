# src-ch2/motion_write_data.py
import numpy as np
import math
from ODEschemes import rk4

""" This script solves the problem with the particle sliding along
    a semicircle:

        theta'' = - mu*(theta')^2 +g/r(cos(theta) - mu*sin(theta))

        
"""

def func(Theta, t):
    
    theta = Theta[0]
    dtheta = Theta[1]
    
    if dtheta >=0:
        out = np.array([dtheta, -mu*dtheta**2 + math.cos(theta) - mu*math.sin(theta)])
        
    elif abs(dtheta)<tol and (abs(mu*math.sin(theta)) - abs(math.cos(theta))>0):
        """If the friction force is higher than the gravity force, and the velocity
            is very close to zero, the ball should not move"""
        out = np.array([0, 0])
    
    else:
        out = np.array([dtheta, mu*dtheta**2 + math.cos(theta) +  mu*math.sin(theta)])
    
    return out

tol=10**-6 # tollerance for zero velocity 

mu_list = np.linspace(0, 1, 11)

Tau = np.linspace(0, 30, 3001)

Theta_0 = np.array([0, 0])
for mu in mu_list:
    
    THETA = rk4(func, Theta_0, Tau)
    theta = THETA[:,0]
    textFile_name = '../data/' + str(mu) + '.txt'
    Tau_write= Tau[0::10]
    theta_write = theta[0::10]
    with open(textFile_name, 'w') as filename:
        for n, tau in enumerate(Tau_write):
            filename.write(str(tau))
            filename.write('    ')
            filename.write(str(theta_write[n]))
            filename.write('\n')
    filename.close()






