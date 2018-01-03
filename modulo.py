distincts = []
for i in range(0, 10):
	s = int(input())
	k = s%42
	if k not in distincts:
		distincts.append(k)

print(len(distincts))