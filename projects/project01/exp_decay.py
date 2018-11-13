import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

class ExponentialDecay:
    def __init__(self,a):
        """Construct an ODE system for exponential decay"""
        self.a = a

    def __call__(self,t,u):
        return -self.a*u

    def __solve(self,u0,T,dt):
        pass
