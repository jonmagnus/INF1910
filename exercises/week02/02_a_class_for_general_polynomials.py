import matplotlib.pyplot as plt
import numpy as np

class Polynomial:
	def __init__(self,coeff):
		self.coeff = coeff

	def __call__(self,x):
		sum_ = 0
		for n in self.coeff.keys():
			sum_ += self.coeff[n]*x**n
		return sum_

	def __str__(self):
		return ' + '.join(['{}*x**{}'.format(self.coeff[a],a) if a != 0 \
			else '{}'.format(self.coeff[a]) \
			for a in sorted(self.coeff.keys(),reverse=True)])

	def __add__(self, other):
		p = Polynomial(self.coeff.copy())
		for a in other.coeff:
			if a not in p.coeff:
				p.coeff[a] = 0
			p.coeff[a] += other.coeff[a]
			if p.coeff[a] == 0: p.coeff.pop(a)
		return p

	def __mul__(self,other):
		coeff = {}
		for a in self.coeff:
			for b in other.coeff:
				if a+b not in coeff:
					coeff[a+b] = 0
				coeff[a+b] += self.coeff[a]*other.coeff[b]
		return Polynomial(coeff)


def derivative(p):
	coeff = {}
	for a in p.coeff:
		if a == 0: continue
		coeff[a-1] = a*p.coeff[a]
	return Polynomial(coeff)

class AddableDict(dict):
	def __add__(self,other):
		ans = self.copy()
		for k in other:
			if k not in ans:
				ans[k] = 0
			ans[k] += other[k]
		return ans

if __name__ == '__main__':
	coeffs = {0:1,5:-1,10:1}
	f = Polynomial(coeffs)

	print 'a)'
	print f

	x = np.linspace(-1,1,101)
	plt.plot(x,f(x))
	plt.show()

	print 'b)'
	f = Polynomial({0:1,5:-7,10:1})
	g = Polynomial({5:7,10:1,15:-3})

	print f+g

	print 'd)'
	print derivative(Polynomial({10:1,6:-3,2:2}))

	print 'e)'
	f = Polynomial({2:4,1:1})
	g = Polynomial({3:3,0:1})
	print f*g
