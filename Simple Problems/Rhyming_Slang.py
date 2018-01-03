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
#phrases = ['tasty sprout','difficult route','worried and fraught','forever in doubt','apples and pears']
count =0
for i in phrases:
	en = i.split()[-1]
	found = 0
	for j in collection:
		if j in en:
			if en[-1] not in word[-1] and en[-2] not in word[-1]:
				break
			else:
				found+=1
			#print('YES')
			break
	if found!=0:
		Yes_and_No.append('YES')
		count+=1
	else:
		Yes_and_No.append('No')

for i in Yes_and_No:
	print(i)