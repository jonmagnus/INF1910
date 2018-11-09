import nose.tools as nt
from e04_testing_median_function import median

@nt.raises(TypeError)
def test_median_type():
	"""Test TypeError spotting in median"""
	median(.2)

@nt.raises(ValueError)
def test_median_empty():
	"""Test spotting for empty data in median"""
	median([])

def test_median():
	"""Test correctness of median"""
	nt.assert_equal(median([1]),1)
	nt.assert_equal(median([36,1]),37/2)
	nt.assert_equal(median((1151,161,5116,125,61,4161,35,14)),(161 + 125)/2)
	l = [5,4,3,2,1];
	nt.assert_equal(median(l),3)
	nt.assert_items_equal(l,[5,4,3,2,1])

if __name__ == '__main__':
	import nose
	nose.run()

