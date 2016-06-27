from math import sqrt
from scipy.special import jv as besselj
import numpy as np

def compute(x, rho, omega, mu):

    R = 0.01
    dpdx = -1
    alpha = R*sqrt(rho*omega/mu)
    
    
    numerator = besselj(0, 1j**1.5*alpha*x/R)
    denominator = besselj(0, 1j**1.5*alpha)
    
    bracket = 1 - numerator/denominator
    coefficient = dpdx*1j/(rho*omega)
    
    profile = coefficient*bracket
    profile = profile.real
    maxValue = np.amax(profile)
    profile = profile/maxValue
    
    return profile

