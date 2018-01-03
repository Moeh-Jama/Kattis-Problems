enter = input()
a = int(enter.split()[0])
res = int(enter.split()[-1])
j  =a
found = True
while found:
	#print(j)
	if (int(j / a) + (j % a > 0) ) == res:
		print(j)
		found=False
		break
	j+=1
#print('found: '+str(j))