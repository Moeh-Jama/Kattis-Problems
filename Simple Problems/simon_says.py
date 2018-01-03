number = int(input())
#sent = ['Simon says raise your right hand.', 'Lower your right hand.', 'Simon says raise your left hand.']
for i in range(0, number):
	enter = []
	get = input()
	enter = get.split()
	if 'Simon' in enter and 'says' in enter:
		enter.pop(0)
		enter.pop(0)
		rep = ''
		for j in enter:
			rep+=j+' '

		print(rep)