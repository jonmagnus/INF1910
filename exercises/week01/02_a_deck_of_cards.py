from random import shuffle

cards = []
for v in range(1,14):
	for s in ['C','H','S','D']:
		cards.append((v,s))

shuffle(cards)
draw = cards[:13]
draw.sort()
print draw

