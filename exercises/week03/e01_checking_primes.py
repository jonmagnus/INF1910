def is_prime(n):
	if not isinstance(n,int):
		raise TypeError('Input has to be integer')
	if n <= 0:
		raise ValueError('Value has to be positive')

	if n == 1: return False
	for i in range(2,n):
		if n % i == 0: return False
	return True


