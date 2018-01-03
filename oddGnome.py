rows = int(input())
g = []
for i in range(0, rows):
	res = (input()).split()
	g.append(res)
#g = [[7,1,2,3,4,8,5,6],[5,3,4,5,2,6],[4,10,20,11,12]]

for i in g:
	i.pop(0)
	i.pop(-1)
	#print(i)
	prev = int(i[0])
	dist = 0
	count = 0
	for j in i:
		current = int(j)
		if current!=prev:
			dist = current-prev
			#print(dist)
			if dist>1 or dist<0:
				break
		prev =current
		count+=1
	print(count+1)