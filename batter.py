a = int(input())
s = input().split()
walks=0
tot=0
for i in s:
	bats = int(i)
	if bats==-1:
		walks+=1
	else:
		tot+=bats
print((tot)/(a-walks))
