while True:
	get = input()
	if get=='0':
		break
	else:
		p = float(get.split()[-1])
		x1  =float(get.split()[0])
		y1  =float(get.split()[1])
		x2  =float(get.split()[2])
		y2  =float(get.split()[3])

		x = (abs(x1-x2))**p
		y= (abs(y1-y2))**p
		res = (x+y)**(1/p)
		if res<0:
			res=res*(-1)
		print(res)