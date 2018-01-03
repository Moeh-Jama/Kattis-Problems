enter = (input()).split()
cases = int(enter[-1])
safety = int(enter[0])
turned_away =0
minus = 0
capacity=safety
for i in range(0, cases):
	group = (input()).split()
	if group[0] =='enter':
		if int(group[-1])  >capacity:
			turned_away+=1
		else:
			#print('minus\t'+str(capacity)+', \t'+str(group[-1]))
			capacity = capacity-int(group[-1])
	elif group[0] == 'leave':
		capacity = capacity+int(group[-1])


print(turned_away)


