import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

g = 9.81

class Pendelum:
    def __init__(self,L=1,M=1):
        self.L = L
        self.M = M

    def __call__(self,t,y):
        """Return the RHS of the ODE"""
        theta, omega = y
        theta_ = omega
        omega_ = -g*np.sin(theta)/self.L
        return (theta_,omega_)
    
    def solve(y0,T,dt,angles='rad'):
        if angles == 'deg':
            y0 = (y[0]*np.pi/180,y[1]*np.pi/180)
        n = int(T/dt)
        t = np.linspace(0,T,n+1)
        sol = solve_ivp(fun=self,t_span=T,y0=y0,t_eval=t)
        self.t = sol.t
        self.y = sol.y
