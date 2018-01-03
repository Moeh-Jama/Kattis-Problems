cases = input()

for j in range(0, int(cases)):
	get = input()
	string = input().split()

	save = []
	dup = []
	for i in string:
		if i not in save:
			save.append(i)
		else:
			dup.append(i)
	number = 1
	for i in string:
		if i not in dup:
			print('Case #'+str(j+1)+': '+i)