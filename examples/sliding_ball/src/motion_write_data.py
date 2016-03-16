# src-ch2/motion_write_data.py
import numpy as np
import math
from ODEschemes import rk4

def func(Theta, t):
    
    theta = Theta[0]
    dtheta = Theta[1]
    
    if dtheta >=0:
        out = np.array([dtheta, math.cos(theta) - mu*math.sin(theta)])
    else:
        out = np.array([dtheta, math.cos(theta) +  mu*math.sin(theta)])
    
    return out

mu_list = np.linspace(0, 1, 11)

Tau = np.linspace(0, 10, 101)

Theta_0 = np.array([0, 0])
for mu in mu_list:
    
    THETA = rk4(func, Theta_0, Tau)
    theta = THETA[:,0]
    textFile_name = '../data/' + str(mu) + '.txt'
    with open(textFile_name, 'w') as filename:
        for n, tau in enumerate(Tau):
            filename.write(str(tau))
            filename.write('    ')
            filename.write(str(theta[n]))
            filename.write('\n')
    filename.close()






