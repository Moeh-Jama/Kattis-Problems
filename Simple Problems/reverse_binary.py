get = input()
def check(g):
	dec = 0
	for digit in g:
		dec = dec*2 + int(digit)
	return dec


#print(check('011'))
k = bin(int(get))[2:]
returned = ''
i = len(k)-1
while i>=0:
	returned+=k[i]
	i-=1
print(check(returned))