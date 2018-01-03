PI = 3.141592654


while True:
	get = input().split()
	#print(PI*(10**2))
	if get[0]=='0' and get[1]=='0' and get[-1]=='0':
		break
	else:
		r = float(get[0])
		m = float(get[1])
		c = float(get[2])
		accurate = PI*(r**2)
		estimate = ((r*2)**2) * (c/m)
		print(str(accurate)+' '+str(estimate))
