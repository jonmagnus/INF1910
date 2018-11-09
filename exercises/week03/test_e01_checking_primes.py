import nose.tools as nt
from E01_checking_primes import is_prime

@nt.raises(TypeError)
def test_is_prime_type():
	"""Test TypeError-spotting"""
	is_prime(.1)

@nt.raises(ValueError)
def test_is_prime_value():
	"""Test ValueError-spotting"""
	is_prime(0)

def test_is_prime():
	"""Test correctness"""
	nt.assert_true(is_prime(2))
	nt.assert_true(is_prime(11))
	nt.assert_false(is_prime(1))
	nt.assert_false(is_prime(6))

if __name__ == '__main__':
	import nose
	nose.run()
