numnber = int(input())
cases = []
for e in range(0, numnber):
	geter = input()
	pep = input()
	get = []
	for i in pep.split():
		get.append(int(i))
	get.sort()

	freq = {}
	for i in get:
		if i not in freq:
			freq[i] = 1
		else:
			freq[i] +=1

	#print(get[0])
	minimum =get[0]
	min_number = get[0]
	for i in freq:
		#print(i)
		if freq[i] < minimum:
			#print(i)
			min_number = i
	print('Case #'+str(e+1)+': '+str(min_number))
