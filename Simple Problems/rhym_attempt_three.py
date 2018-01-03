enter = 'stairs'
n = 'erres airs ears ares aires'.split()
e = 'eet eat'.split()
phrases = ['apples and pears', 'plates of meat']
word_endings = []
p_1 = []
for i in n:
	#print(i)
	print(str(len(enter))+' '+str(len(i)))
	if len(enter) < len(i):
		print(i)
	elif enter[len(enter)-len(i)] == enter:
		p_1.apppend(i)
for i in e:
	#print(i)
	print(str(len(enter))+' '+str(len(i)))
	if len(enter) < len(i):
		print(i)
	elif enter[len(enter)-len(i)] == enter:
		p_1.apppend(i)
print(p_1)
for i in phrases:
	en = i.split()[-1]
	found = False
	