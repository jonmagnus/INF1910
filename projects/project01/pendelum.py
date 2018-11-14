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
        self._x = None
        self._y = None
        self._potential = None
        self._kinetic = None
        self._vx = None
        self._vy = None

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
        self._x = [self.L*np.sin(theta) for theta in self._theta]
        self._y = [-self.L*np.cos(theta) for theta in self._theta]
        self._potential = [self.M*g*(y + self.L) for y in self._y]
        self._vx = np.gradient(self._x, self._t)
        self._vy = np.gradient(self._y, self._t)
        self._kinetic = [.5*self.M*(v[0]**2 + v[1]**2) for v in zip(self._vx,self._vy)]

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

    @property
    def x(self):
        if self._x is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._x

    @property
    def y(self):
        if self._y is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._y
    
    @property
    def potential(self):
        if self._potential is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._potential
 
    @property
    def kinetic(self):
        if self._kinetic is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._kinetic
 
    @property
    def vx(self):
        if self._vx is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._vx
 
    @property
    def vy(self):
        if self._vy is None:
            raise UnsolvedError("This ODE has not yet been solved")
        return self._vy

class DampenedPendelum(Pendelum):
    def __init__(self,L=1,M=1,B=0):
        super().__init__(L=L,M=M)
        self.B = B

    def __call__(self,t,y):
        """Return the RHS of the ODE"""
        theta, omega = y
        theta_ = omega
        omega_ = -g*np.sin(theta)/self.L - self.B*omega/self.M
        return (theta_,omega_)
 

if __name__ == '__main__':
    pend = DampenedPendelum()
    pend.solve((np.pi/2,0),3,.01)
    
    plt.figure()
    plt.title('Position')
    plt.xlabel('x / m')
    plt.ylabel('y / m')
    plt.axis('equal')
    plt.plot(pend.x,pend.y)
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.title('Angle')
    plt.xlabel('time / s')
    plt.ylabel('angle')
    plt.plot(pend.t,pend.theta)

    plt.subplot(2,1,2)
    plt.title('Energy')
    plt.xlabel('time / s')
    plt.ylabel('energy / J')
    plt.plot(pend.t,pend.potential,label='Potential')
    plt.plot(pend.t,pend.kinetic,label='Kinetic')

    plt.legend()
    plt.show()

