import nose.tools as nt
from scipy.integrate import solve_ivp
from exp_decay import ExponentialDecay

def test_init():
    decay_model = ExponentialDecay(.4)
    nt.assert_almost_equal(decay_model(0,3.2),-1.28)

if __name__ == '__main__':
    import nose
    nose.run()
