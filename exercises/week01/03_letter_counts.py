def count_chars(inp_str):
	ans = {}
	inp_str.lower()
	for c in inp_str:
		if c not in ans:
			ans[c] = 0
		ans[c] += 1
	return ans

example = "Hello, world!"

print 'Non-specific order:'
for char, count in count_chars(example).items():
        print '{:3}{:10}'.format(char,count)

print 'Alphabetical order:'
for char, count in sorted(count_chars(example).items()):
	print '{:3}{:10}'.format(char,count)

print 'Ordered by occurance (then alphabetically):'
for count, char in sorted([(-p[1],p[0]) for p in count_chars(example).items()]):
	print '{:3}{:10}'.format(char,-count)	# Negate the answer to reverse order of integer sort
