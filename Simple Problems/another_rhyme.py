Yeses_and_Nos = []
def rhymes(w, e, num):
	res =0
	i = len(w)-1
	while i> 0:
		if w[i] in e:
			res+=1
		i-=1
	if res>=num:
		return 1
	else:
		return 0

def testing_phrases(w, e, catcher, num):
	res = 0
	if catcher == 'first':
		i = len(e)-1
		if e[i] not in w[-1]:
			if len(e) >=1:
				if e[i-1] not in w[-1]:
					return -1
				else:
					return 1
			return -1
		else:
			return 1
	else:
		k = len(w)-1
		while k >= 0:
			if w[k] in e:
				res +=1
			k-=1
	if res >= num:
		return 1

word = input()
number_of_rows = int(input())
a_count = 0
for i in range(0, number_of_rows):
	entered = input()
	kount = 0
	for j in entered.split():
		kount+= rhymes(word, entered, 1)
	if kount == len(entered.split()):
		a_count+=1
		#Yeses_and_Nos.append('YES')
	#else:
		#Yeses_and_Nos.append('NO')


num = int(input())
kount = 0
for i in range(0, num):
	phrase = input()
	arr = phrase.split()
	i = len(phrase.split())-1
	irrevelent = 0
	count = 0
	while i >= 0 :
		if arr[i].strip()!= 'in' and arr[i].strip()!='and' and arr[i]!='or' and arr[i]!='of':
			if i == len(phrase.split())-1:
				count += testing_phrases(list(word), arr[i], 'first', 0)
				if testing_phrases(list(word), arr[i], 'first', 0) == -1:
					count = -1
					break
			else:
				count += testing_phrases(list(word), arr[i], 'other', 1)
		else:
			irrevelent+=1
		i-=1
	if count==-1:
		Yeses_and_Nos.append('NO')
	elif count<= len(phrase.split())-irrevelent:
		Yeses_and_Nos.append('YES')
	else:
		Yeses_and_Nos.append('NO')
for i in Yeses_and_Nos:
	print(i)