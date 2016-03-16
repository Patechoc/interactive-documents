# src-ch2/motion.py
import matplotlib; matplotlib.use('Qt4Agg')
import matplotlib.pylab as plt
plt.get_current_fig_manager().window.raise_()
import numpy as np
import math
from ODEschemes import rk4
from myanimation import animatePendulum



#### set default plot values: ####
#LNWDT=5; FNT=15
#plt.rcParams['lines.linewidth'] = LNWDT; plt.rcParams['font.size'] = FNT

""" This script solves the problem with the particle sliding along
    a semicircle:

        theta'' = - mu*(theta')^2 +g/r(cos(theta) - mu*sin(theta))

        
"""

def func(Theta, t):
    
    theta = Theta[0]
    dtheta = Theta[1]
    
    if dtheta >=0:
        out = np.array([dtheta, math.cos(theta) - mu*math.sin(theta)])
    else:
        out = np.array([dtheta, math.cos(theta) +  mu*math.sin(theta)])
    
    return out

mu = 0.4

Tau = np.linspace(0, 10, 101)

Theta_0 = np.array([0, 0])

THETA = rk4(func, Theta_0, Tau)

animatePendulum(THETA[:,0], Tau, l=1)





