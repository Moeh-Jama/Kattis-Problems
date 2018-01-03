rows = int(input())
for j in range(0, rows):
	seq = input().split()

	current = int(seq[0])
	prev = int(seq[0])
	imports=0
	i = 0
	while i < len(seq)-1:
		current=int(seq[i])
		if (prev*2)<current:
			#print(str(prev*2)+', '+str(current))
			imports+= current - (prev*2)
		prev=current
		#print(current)


		i+=1
	print(imports)