def fibonacci(n):
	if n == 0: return 0
	if n == 1: return 1
	return fibonacci(n-1) + fibonacci(n-2)

class Fibonacci:
	def __init__(self):
		self.memory = {0:0,1:1}

	def __call__(self,n):
		if n not in self.memory:
			self.memory[n] = self(n-1) + self(n-2)
		return self.memory[n]

	def avoid_max_depth(self,n):
		for i in range(max(self.memory.keys()),n):
			self(i)
		return self(n)

class Factorial:
	def __init__(self):
		self.memory = {0:1}

	def __call__(self,n):
		if n not in self.memory:
			self.memory[n] = n*self.memory[n-1]
		return self.memory[n]

if __name__ == '__main__':
	print 'a)'
	print [fibonacci(i) for i in range(1,11)]

	print 'b)'
	fib = Fibonacci()
	print fib(100)

	print 'c)'
	print fib.avoid_max_depth(100000)

	print 'd)'
	fac = Factorial()
	print [fac(i) for i in range(11)]
