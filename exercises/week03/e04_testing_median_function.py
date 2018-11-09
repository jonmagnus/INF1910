def median(data):
	"""Returns the median of a dataset."""
	if not isinstance(data,(list,tuple)):
		raise TypeError('Input must be a list')
	if len(data) < 1:
		raise ValueError('Input must contain at least one element')
	data_ = sorted(data)[:]
	return (data_[len(data)//2] + data_[(len(data)-1)//2])/2
