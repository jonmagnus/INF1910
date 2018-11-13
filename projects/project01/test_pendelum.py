import nose.tools as nt
import numpy as np
from pendelum import Pendelum
from math import pi

def test_init():
    """Test call of Pendelum-class"""
    p = Pendelum(L=2.2)
    y1 = p(0,(.1,pi/4))
    nt.assert_almost_equal(y1[0],pi/4)
    nt.assert_almost_equal(y1[1],-9.81*np.sin(.1)/2.2)
    y2 = p(0,(0,0))
    nt.assert_almost_equal(y2[0],0)
    nt.assert_almost_equal(y2[1],0)

if __name__ == '__main__':
    import nose
    nose.run()
