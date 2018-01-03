numbers = input().split()
i = 2
a = ''
b = ''
while i>=0:
	a += numbers[0][i]
	b += numbers[1][i]
	i-=1
print(max(a,b))