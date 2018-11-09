import nose.tools as nt
from e02_writing_bubble_sort import bubble_sort

@nt.raises(TypeError)
def test_bubble_sort_type():
	"""Test TypeError-spotting for bubble_sort."""
	bubble_sort(1)

@nt.raises(TypeError)
def test_bubble_sort_arguments():
	"""Test if bubble_sort rejects multiple arguments."""
	bubble_sort(1,2,3)

def test_bubble_sort():
	"""Test the correctness of bubble_sort."""
	tl = [4,1,7,16,7,26,6167,1,54]
	for p in zip(bubble_sort(tl),sorted(tl)):
		nt.assert_equal(p[0],p[1])
	for p in zip(tl,[4,1,7,16,7,26,6167,1,54]):
		nt.assert_equal(p[0],p[1])
	nt.assert_items_equal(bubble_sort([]),[])
	nt.assert_items_equal(bubble_sort([-10000]),[-10000])

if __name__ == '__main__':
	import nose
	nose.run()
