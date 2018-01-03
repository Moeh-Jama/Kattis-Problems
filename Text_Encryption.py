while True:
	transposition = int(input())
	if transposition==0:
		break
	msg = input().upper().split()
	#goal = 'CMTMUIONPGECNOPNRTOEGSRTA'
	#		'CTUOPENPROGRAMMINGCONTEST'
	string = ''
	for i in msg:
		for j in i:
			string+=j
	#print(string)
	conversion = list(string)
	def decrypt(a,s):
		if s==1:
			return [a]
		else:
			#print(a[:int(len(a)/s)])
			k = a[:int(len(a)/s)+1]
			#string = []
			string = decrypt(a[int(len(a)/s)+1:], s-1)
			return [k]+string
	e = decrypt(conversion, transposition)
	#Find smallest row of e
	string = ''
	for i in range(len(e[0])):
		for j in e:
			if i< len(j):
				print(j[i], end='')
	print(string)