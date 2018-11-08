from random import randint

def factorize(n):
	factors = []
	while (n > 1):
		for i in range(2,n + 1):
			if n % i != 0: continue
			n /= i
			factors.append(i)
			break
	return factors


print 'the factors of ', 23,' are ', factorize(23)
print 'the factors of ', 18,' are ', factorize(18)
n = randint(100000,1000000)
print 'the factors of ', n,' are ', factorize(n)
