enter = 'octopuses'

count=0
i = 0
'''
while i < len(enter):
	#print(enter[i])
	if i<len(enter)-1 and (enter[i].lower() == enter[i+1].lower()) and enter[i].lower()=='s':
		print('hiss')
		count=1
		break
	i+=1
if count!=1:
	print('no hiss')
'''
if 'ss' in enter:
	print('hiss')
else:
	print('no hiss')