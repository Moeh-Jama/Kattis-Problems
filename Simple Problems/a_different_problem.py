enter = input()
def res(a, b):
	if a>b:
		return a-b
	else:
		return b-a
take = enter.split()
print(res(float(take[0]), float(take[-1])))


