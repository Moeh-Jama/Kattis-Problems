entered = []
for i in range(0, 5):
	st = input()
	entered.append(st)

results = []
for i in entered:
	k = 0
	for j in i.split():
		k+=int(j)
	results.append(k)

max_index = 0
maximum = results[0]
i = 0
while i< len(results):
	if maximum < results[i]:
		maximum = results[i]
		max_index = i
	i+=1

print(str(max_index+1)+' '+str(maximum))