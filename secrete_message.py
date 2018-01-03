testCases = int(input())
for z in range(testCases):
	msg = input()
	L = len(msg)
	M = L
	K=0
	i = 1
	while i < L*20:
		if (i**2) >=L:
			K=i
			M = i**2
			break
		i+=1

	number_of_asteriks = (M-L)
	asteriks = ''
	for h in range(number_of_asteriks):
		asteriks+='*'

	msg+=asteriks
	matrix = []
	i=0
	letters = 0
	while i < K:

		j=0
		s= []
		while j<K:
			s.append(msg[letters])
			letters+=1
			j+=1
		matrix.append(s)
		i+=1
	newMsg=''
	i = 0
	while i<K:
		j = K-1
		while j>=0:
			if matrix[j][i]!= '*':
				newMsg+=matrix[j][i]
			j-=1
		i+=1
	print(newMsg)