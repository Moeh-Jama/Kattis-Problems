list_it = 1
keep = True
while keep==True:
	rows = int(input())
	if rows ==0:
		break
	animals = {}
	found = False
	for i in range(0, rows):
		get = input().split()
		if get[-1].lower() not in animals:
			animals[get[-1].lower()] = 1
		else:
			animals[get[-1].lower()] += 1
	print('List '+str(list_it)+':')
	for i in sorted(animals):
		print(i+' | '+str(animals[i]))
	list_it+=1


