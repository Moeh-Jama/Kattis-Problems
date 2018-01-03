def reverse(n):
	z =''
	i = len(n)-1
	while i>=0:
		z+=(n[i])
		i-=1
	return z

a = reverse(list(input()))
b = reverse(list(input()))


def getCollisionAfter(x,y):
	i = 0
	nA = ''
	nB = ''
	while i<len(y):
		if int(y[i]) > int(x[i]):
			nB+=y[i]
		elif int(y[i]) < int(x[i]):
			nA+= x[i]
		else:
			#print(a[i]+' - '+b[i]+'\t'+nA+' - '+nB)
			nA+= x[i]
			nB+=y[i]
		i+=1
	#print(str(x[i:]))
	if i<len(x):
		nA+=x[i:]
	if nA=='':
		nA='YODA'
	if nB=='':
		nB='YODA'

	if nA=='YODA' and nB!='YODA':
		return['YODA', int(reverse(nB))]
	elif nA!='YODA' and nB=='YODA':
		return[int(reverse(nA)), 'YODA']
	elif nA=='YODA' and nB=='YODA':
		return ['YODA', 'YODA']
	else:
		return [int(reverse(nA)), int(reverse(nB))]

if len(a)>=len(b):
	res = getCollisionAfter(a,b)
	print(str(res[0])+'\n'+str(res[1]))
else:
	res = getCollisionAfter(b,a)
	print(str(res[1])+'\n'+str(res[0]))