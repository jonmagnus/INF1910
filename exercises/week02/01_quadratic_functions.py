import matplotlib.pyplot as plt
import numpy as np

class Quadratic:
	def __init__(self,a_2,a_1,a_0):
		self.a_2 = a_2
		self.a_1 = a_1
		self.a_0 = a_0

	def __call__(self,x):
		return (self.a_2*x + self.a_1)*x + self.a_0

	def __str__(self):
		return '{}*x**2 + {}*x + {}'.format(self.a_2, self.a_1, self.a_0)

	__repr__ = __str__

	def __add__(self,other):
		return Quadratic(self.a_2 + other.a_2,
				self.a_1 + other.a_1,
				self.a_0 + other.a_0)

	def roots(self):
		D = self.a_1**2 - 4*self.a_2*self.a_0
		if D == 0:
			return [-self.a_1/(self.a_2*2)]
		if D > 0:
			return [(-self.a_1 + k*np.sqrt(D))/(2*self.a_2) for k in [-1,1]]
		return []

	def __neg__(self):
		return Quadratic(-self.a_2,-self.a_1,-self.a_0)

	def __sub__(self,other):
		return self + (-other)

	def intersect(self,other):
		return (self-other).roots()

if __name__ == '__main__':
	plt.title('a-c')
	f = Quadratic(1,-2,1)
	x = np.linspace(-5,5,101)
	plt.plot(x,f(x),'-.',label=f)
	#plt.legend()
	#plt.show()

	g = Quadratic(-1,6,-3)
	plt.plot(x,g(x),'--',label=g)

	h = f + g

	x = np.linspace(-5,5,101)
	plt.plot(x,h(x),label=h)
	plt.legend()
	plt.show()

	print 'd)'
	print Quadratic(2,-2,2).roots()
	print Quadratic(1,-2,1).roots()
	print Quadratic(1,-3,2).roots()

	print 'e'
	f = Quadratic(1,-2,1)
	g = Quadratic(-2,4,-2)

	print f.intersect(g)

	plt.figure()
	plt.plot(x,f(x),label=f)
	plt.plot(x,g(x),label=g)
	plt.legend()
	plt.show()
