import numpy as np

def slinger(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

y0 = [np.pi/2,1]
print(slinger(y0,1,0,0))



