import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

class ExponentialDecay:
    def __init__(self,a):
        """Construct an ODE system for exponential decay."""
        self.a = a

    def __call__(self,t,u):
        """Retern the RHS of the ODE."""
        return -self.a*u

    def solve(self,u0,T,dt):
        """Return the solution of the ODE with specified parameters."""
        n = int(T/dt)
        t = np.linspace(0,T,n+1)
        sol = solve_ivp(fun=self,t_span=[0,T],y0=(u0,),t_eval=t)
        return sol.t,sol.y[0]   # There is only one y-value to return

if __name__ == '__main__':
    decay_model = ExponentialDecay(.4)
    t,u = decay_model.solve(1000,10,.1)

    plt.plot(t,u)
    plt.show()
