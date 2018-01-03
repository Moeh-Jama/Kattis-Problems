number = int(input())
cases = ['0 100 70', '100 130 30', '-100 -70 40']
for i in range(0, number):
	rep = input()
	r = int(rep.split()[0])
	e = int(rep.split()[1])
	c = int(rep.split()[-1])
	if r < (e-c):
		print('advertise')
	elif r == (e-c):
		print('does not matter')
	else:
		print('do not advertise')