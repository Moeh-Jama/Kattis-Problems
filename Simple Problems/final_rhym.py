word = input()
number_train = int(input())
collection = []
for i in range(0, number_train):
	train = input()
	for j in train.split():
		collection.append(j)
Yes_and_No = []
number_phrases_train = int(input())
phrases=[]
for i in range(0, number_phrases_train):
	train = input()
	phrases.append(train)
def test_phrase_section(endings, phrase, w):
	exclude = ['or', 'of', 'and', 'from', 'not']
	ex = 0
	count = 0
	for p in phrase.split():
		if p not in exclude:
			for j in endings.split():
				#print(p+', '+j)
				if j in p:
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
