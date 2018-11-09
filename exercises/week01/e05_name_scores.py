infile = open('names.txt','r')
names = sorted([eval(s) for s in infile.readline().split(',')])

def name_score(s):
	sum_ = 0
	for c in s:
		sum_ += (ord(c)-ord('A')) + 1
	return sum_

sum_ = 0
for i in range(len(names)):
	sum_ += (i+1)*name_score(names[i])

print sum_
