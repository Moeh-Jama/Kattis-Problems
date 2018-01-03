word = 'stairs'
s = 'erres airs ears ares aires'
e = 'eet eat'
collection = []
collection.append(s)
collection.append(e)
'''
for i in s.split():
	collection.append(i.strip())

for i in e.split():
	collection.append(i.strip())

for i in collection:
	print(i)
'''
Yes_and_No = []
phrases = ['apples and pears','plates of meat']#['tasty sprout','difficult route','worried and fraught','forever in doubt','apples and pears']#['apples and pears','plates of meat']
count =0
def test_phrase_section(endings, phrase, w):
	exclude = ['or', 'of', 'and', 'from', 'not']
	ex = 0
	count = 0
	for p in phrase.split():
		if p not in exclude:
			for j in endings.split():
				#print(p+', '+j)
				if j in p:
					print(j+', '+p)
					count+=1
					break
		else:
			ex +=1
	if count >= len(phrase.split())-ex:
		if phrase[-1] == w[-1] or phrases[-2] == w[-1]:
			return 'YES'
		return 'NO'
	else:
		return 'NO'
for i in phrases:
	#print(i.split()[-1])
	reply = []
	for j in collection:
		reply.append(test_phrase_section(j ,i.split()[-1], word))
	if 'YES' in reply:
		Yes_and_No.append('YES')
	else:
		Yes_and_No.append('NO')

for i in Yes_and_No:
	print(i)
