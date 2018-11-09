def bubble_sort(orig_l):
	"""Sorts a list of numbers."""
	if not isinstance(orig_l,list):
		raise TypeError('bubble_sort only accepts list as argument')
	l = orig_l[:]
	for n in range(0,len(l)-1,-1):
		for i in range(n-1):
			if l[i] > l[i+1]:
				t = l[i]
				l[i] = l[i+1]
				l[i+1] = l[i]
	return l
