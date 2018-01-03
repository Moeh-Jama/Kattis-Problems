'''
Hilbert
Godel
Poincare
Ramanujan
Pochhammmer
'''
while True:
	t = input()
	if t=='0':
		break
	students = []
	for i in range(int(t)):
		req = input()
		students.append(req)
	sorting = {}
	for i in students:
		if i[:2] in  sorting:
			k = sorting[i[:2]]
			string = []
			for j in k:
				string.append(j)
			string.append(i)
			sorting[i[:2]] = string
		else:
			sorting[i[:2]] = [i]
	newArray = []
	for j in sorting:
		newArray.append(j)
	newArray.sort()
	for i in newArray:
		#print(sorting[i])
		for j in range(len(sorting[i])):
			print(sorting[i][j])
	