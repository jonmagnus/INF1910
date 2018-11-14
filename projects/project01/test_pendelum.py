import nose.tools as nt
import numpy as np
from pendelum import Pendelum
from math import pi
from ode_exceptions import UnsolvedError

def test_init():
    """Test call of Pendelum-class"""
    p = Pendelum(L=2.2)
    y1 = p(0,(.1,pi/4))
    nt.assert_almost_equal(y1[0],pi/4)
    nt.assert_almost_equal(y1[1],-9.81*np.sin(.1)/2.2)
    y2 = p(0,(0,0))
    nt.assert_almost_equal(y2[0],0)
    nt.assert_almost_equal(y2[1],0)

@nt.raises(UnsolvedError)
def test_t():
    """Test if unsolved ODE raises proper exeption when getting t."""
    p = Pendelum()
    p.t()

@nt.raises(UnsolvedError)
def test_theta():
    """Test if unsolved ODE raises proper exeption when getting theta."""
    p = Pendelum()
    p.theta()
    
@nt.raises(UnsolvedError)
def test_omega():
    """Test if unsolved ODE raises proper exeption when getting omega."""
    p = Pendelum()
    p.omega()

def test_solve():
    """Test if solution-arrays of ODE are reasonable."""
    p = Pendelum()
    p.solve((0,0),T=10,dt=.1)
    t = np.linspace(0,10,101)
    for z in zip(p.t,t):
        nt.assert_almost_equal(z[0],z[1])
    for theta in p.theta:
        nt.assert_almost_equal(theta,0)
    for omega in p.omega:
        nt.assert_almost_equal(omega,0)

def test_lenght_constant():
    """Test if the length is preserved after changing coordinates."""
    p = Pendelum()
    p.solve(y0=(pi/2,0),T=10,dt=.1)
    for x,y in zip(p.x,p.y):
        nt.assert_almost_equal(x*x + y*y,p.L*p.L)

if __name__ == '__main__':
    import nose
    nose.run()
