import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from ode_exceptions import UnsolvedError

g = 9.81

class DoublePendelum:
    def __init__(self,M1=1,L1=1,M2=1,L2=1):
        self.M1 = M1
        self.L1 = L1
        self.M2 = M2
        self.L2 = L2
        self._t = None
        self._theta1 = None
        self._omega1 = None
        self._theta2 = None
        self._omega2 = None
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._potential = None
        self._vx1 = None
        self._vy1 = None
        self._vx2 = None
        self._vy2 = None
        self._kinetic = None

    def __call__(self,t,y):
        theta1,omega1,theta2,omega2 = y
        diff_theta = theta2 - theta1

        theta1_ = omega1
        theta2_ = omega2

        omega1_ = (self.M2*self.L1*omega1**2*np.sin(diff_theta)*np.cos(diff_theta)
                   + self.M2*g*np.sin(theta2)*np.cos(diff_theta)
                   + self.M2*self.L2*omega2**2*np.sin(diff_theta)
                   - (self.M1 + self.M2)*g*np.sin(theta1)
                  )/(
                  (self.M1 + self.M2)*self.L1
                   - self.M2*self.L1*np.cos(diff_theta)**2)
        omega2_ = (-self.M2*self.L2*np.sin(diff_theta)*np.cos(diff_theta)
                   + (self.M1 + self.M2)*g*np.sin(theta1)*np.cos(diff_theta)
                   - (self.M1 + self.M2)*self.L1*omega1**2*np.sin(diff_theta)
                   - (self.M1 + self.M2)*g*np.sin(theta2)
                  )/(
                   (self.M1 + self.M2)*self.L2
                   - self.M2*self.L2*np.cos(diff_theta)**2)
        
        return (theta1_,omega1_,theta2_,omega2_)

    def solve(self,y0,T,dt,angles='rad'):
        if angles == 'deg':
            y0 = tuple([y*np.pi/180 for y in y0])
        n = int(T/dt)
        t = np.linspace(0,T,n+1)
        sol = solve_ivp(fun=self,t_span=(0,T),y0=y0,t_eval=t,method='Radau')
        self._t = sol.t
        self._theta1 = sol.y[0]
        self._omega1 = sol.y[1]
        self._theta2 = sol.y[2]
        self._omega2 = sol.y[3]
        self._x1 = [self.L1*np.sin(theta1) for theta1 in self._theta1]
        self._y1 = [-self.L1*np.cos(theta1) for theta1 in self._theta1]
        self._x2 = [x1 + self.L2*np.sin(theta2) for x1,theta2 in zip(self._x1,self._theta2)]
        self._y2 = [y1 - self.L2*np.cos(theta2) for y1,theta2 in zip(self._y1,self._theta2)]
        self._potential = [self.M1*g*(y1 + self.L1) + self.M2*g*(y2 + self.L1 + self.L2) \
                           for y1,y2 in zip(self._y1,self._y2)]
        self._vx1 = np.gradient(self._x1,self._t)
        self._vy1 = np.gradient(self._y1,self._t)
        self._vx2 = np.gradient(self._x2,self._t)
        self._vy2 = np.gradient(self._y2,self._t)
        self._kinetic = [.5*(self.M1*(vx1*vx1 + vy1*vy1) + self.M2*(vx2*vx2 + vy2*vy2)) \
                         for vx1,vy1,vx2,vy2 in zip(self._vx1,self._vy1,self._vx2,self._vy2)]
    
    @property
    def t(self):
        if self._t is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._t
    
    @property
    def theta1(self):
        if self._theta1 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._theta1
    
    @property
    def omega1(self):
        if self._omega1 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._omega1
    
    @property
    def theta2(self):
        if self._theta2 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._theta2
    
    @property
    def omega2(self):
        if self._omega2 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._omega2

    @property
    def x1(self):
        if self._x1 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._x1
    
    @property
    def y1(self):
        if self._y1 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._y1

    @property
    def x2(self):
        if self._x2 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._x2
    
    @property
    def y2(self):
        if self._y2 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._y2
    
    @property
    def potential(self):
        if self._potential is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._potential
    
    @property
    def vx1(self):
        if self._vx1 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._vx1
    
    @property
    def vy1(self):
        if self._vy1 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._vy1
    
    @property
    def vx2(self):
        if self._vx2 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._vx2
    
    @property
    def vy2(self):
        if self._vy2 is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._vy2
    
    @property
    def kinetic(self):
        if self._kinetic is None:
            raise UnsolvedError('This ODE has not yet been solved')
        return self._kinetic


if __name__ == '__main__':
    pend = DoublePendelum(L1=2)
    pend.solve((np.pi/2,0,-np.pi/2,0),3,.01)
    
    plt.title('Position')
    plt.xlabel('x / m')
    plt.ylabel('y / m')
    plt.axis('equal')
    plt.plot(pend.x1,pend.y1)
    plt.plot(pend.x2,pend.y2)
    
    plt.show()

