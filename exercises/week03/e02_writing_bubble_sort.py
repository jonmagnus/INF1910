def bubble_sort(orig_list):
	"""Sorts a list of numbers."""
	if not isinstance(orig_list,list):
		raise TypeError('bubble_sort only accepts list as argument')
	new_list = orig_list[:]
	for n in range(0,len(new_list)-1,-1):
		for i in range(n-1):
			if new_list[i] > new_list[i+1]:
				t = new_list[i]
				new_list[i] = new_list[i+1]
				new_list[i+1] = new_list[i]
	return new_list
