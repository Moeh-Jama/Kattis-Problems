number = int(input())
count = 0
for i in range(0, number):
	j = 0
	e = 0
	sen = ''
	num = 0
	rep = input()
	while j<len(rep)-1:
		sen+=rep[j]
		j+=1
	e = int(rep[j])
	num = int(sen)
	count+= num**e
	#print(arr[i])
print(count)