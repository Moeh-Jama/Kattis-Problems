t = 'abc def ghi jkl mno pqrs tuv wxyz'.split()
alpha = {}

for i in t:
	k =0
	for j in i:
		alpha[j]=(k+1)
		k+=1

print(alpha)
enter = 'good luck and have fun'
total = 0
for i in enter:
	if i != ' ':
		print(i, end='')
		total+=alpha[i]
	else:
		total+=1
		print(' ', end=' ')
print()
print(total)