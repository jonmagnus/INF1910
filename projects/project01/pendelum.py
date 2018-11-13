import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from ode_exeptions import UnsolvedError

g = 9.81

class Pendelum:
    def __init__(self,L=1,M=1):
        self.L = L
        self.M = M
        self._t = None
        self._theta = None
        self._omega = None

    def __call__(self,t,y):
        """Return the RHS of the ODE"""
        theta, omega = y
        theta_ = omega
        omega_ = -g*np.sin(theta)/self.L
        return (theta_,omega_)
    
    def solve(self,y0,T,dt,angles='rad'):
        if angles == 'deg':
            y0 = (y0[0]*np.pi/180,y0[1]*np.pi/180)
        n = int(T/dt)
        t = np.linspace(0,T,n+1)
        sol = solve_ivp(fun=self,t_span=(0,T),y0=y0,t_eval=t)
        self._t = sol.t
        self._theta = sol.y[0]
        self._omega = sol.y[1]

    @property
    def t(self):
        if self._t is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._t
 
    @property
    def theta(self): 
        if self._theta is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._theta

    @property
    def omega(self): 
        if self._omega is None:
             raise UnsolvedError("This ODE has not yet been solved")
        return self._omega

