total = int(input())
collection = []
for i in range(0, total):
	rep = input()
	collection.append(rep)
total_average = 0

totals = []
students = []
average = []
n = 0
for i in collection:
	en = 0
	students.append(i.split()[0])
	n=int(i.split()[0])
	tot = 0
	for j in i.split()[1:]:
		en += int(j)
	average.append((1/n)*en)
k=0

for i in collection:
	f=0
	t = float(i.split()[0])
	for j in i.split()[1:]:
		if float(j) > average[k]:
			f+=1
	print("%0.3f" % round((f/t)*100, 3),end='')
	print('%')
	k+=1
