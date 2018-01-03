
cards = {
	'T':0,
	'C':0,
	'G':0
}

enter = input()
total = 0
for i in enter:
	if i in cards:
		cards[i]+=1
		total+=1
bonus = 7
final = 0
for i in cards:
	final+= cards[i]**2
k = 0
k = min(cards['T'], cards['C'], cards['G'])
print(final+(bonus*k))