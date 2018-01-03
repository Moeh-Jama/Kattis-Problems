entered ='5 15 3'
a = int(entered.split()[0])
b = int(entered.split()[1])
res = int(entered.split()[-1])
if a+b == res:
	print(str(a)+'+'+str(b)+'='+str(res))
elif a*b == res:
	print(str(a)+'*'+str(b)+'='+str(res))
elif a/b == res:
	print(str(a)+'+'+str(b)+'='+str(res))

elif a == b*res:
	print(str(a)+'='+str(b)+'*'+str(res))

elif a == b/res:
	print(str(a)+'='+str(b)+'/'+str(res))

elif a == b+res:
	print(str(a)+'='+str(b)+'+'+str(res))

elif b == a*res:
	print(str(b)+'='+str(a)+'*'+str(res))

elif b == a/res:
	print(str(b)+'='+str(a)+'/'+str(res))

elif b == a+res:
	print(str(b)+'='+str(a)+'+'+str(res))