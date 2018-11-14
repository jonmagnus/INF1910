import nose.tools as nt
import numpy as np
from double_pendelum import DoublePendelum
from ode_exceptions import UnsolvedError

def test_call():
    """Test call of DoublePendelum-class"""
    pend = DoublePendelum()
    y = pend(0,(0,0,0,0))
    for v in y:
        nt.assert_almost_equal(v,0)

@nt.raises(UnsolvedError)
def test_t():
    """Test if unsolved ODE raises proper exception from DoublePendelum"""
    pend = DoublePendelum()
    pend.t()

def test_solve():
    pend = DoublePendelum()
    pend.solve((0,0,0,0),T=10,dt=.1)
    t = np.linspace(0,10,101)
    for t1,t2 in zip(pend.t,t):
        nt.assert_almost_equal(t1,t2)
    for theta1 in pend.theta1:
        nt.assert_almost_equal(theta1,0)
    for omega1 in pend.omega1:
        nt.assert_almost_equal(omega1,0)
    for theta2 in pend.theta2:
        nt.assert_almost_equal(theta2,0)
    for omega2 in pend.omega2:
        nt.assert_almost_equal(omega2,0)

if __name__ == '__main__':
    import nose
    nose.run()
