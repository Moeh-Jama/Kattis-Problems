iterations = int(input())
for k in range(0, iterations):
	rows = input()
	enter = (input()).split()
	new = []

	for i in enter:
		new.append(int(i))

	new.sort()
	top = new[0]
	count = 0

	current = new[0]
	prev = new[0]
	t=0
	for i in new:
		current=i
		if t==0:
			t+=1
		else:
			a = max(current, prev)
			b = min(current, prev)
			count +=a-b
			prev = current

	print(count+(new[-1]-top))