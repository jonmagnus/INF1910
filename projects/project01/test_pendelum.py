import nose.tools as nt
import numpy as np
from pendelum import Pendelum
from math import pi
from ode_exeptions import UnsolvedError

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

if __name__ == '__main__':
    import nose
    nose.run()
