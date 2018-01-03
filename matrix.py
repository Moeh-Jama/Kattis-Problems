case =1
while True:
	try:
		f0 = input().split()
		f1 = input().split()
		s =input()
		a = int(f0[0])
		b = int(f0[1])
		c = int(f1[0])
		d = int(f1[1])
		det = 1 / ((a*d) - (b*c))
		#print(det)
		adj0 = str(int(det*d))+' '+str(int(det*-b))
		adj1 = str(int(det*-c))+' '+str(int(det*a))
		print('Case '+str(case)+':')
		print(adj0)
		print(adj1)
		case+=1
	except EOFError:
		break