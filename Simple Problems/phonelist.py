number = int(input())
#entered = ['911', '97625999','91125426']

yeses = []
for test_cases in range(0, number):
	found = False
	gathered = []
	test = int(input())
	for en in range(0, test):
		entered = input().split()
		dup = False
		for i in entered:
			if len(gathered)>0:
				if gathered[0] in  i[0:len(gathered[0])]:
					found = True
					yeses.append('NO')
					dup = True
				else:
					gathered.append(i)
			else:
				gathered.append(i)
	if found == False:
		yeses.append('YES')

for k in yeses:
	print(k)