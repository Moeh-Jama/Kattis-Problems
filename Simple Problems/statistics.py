#number_of_test_cases = int(input())
cases = []
k = 1
while True:
	rep = input()
	curr = int(rep.split()[0])
	minimum = int(rep.split()[1])
	maximum = int(rep.split()[1])
	for i in rep.split()[1:]:
		#print(i)
		if minimum > int(i):
			minimum = int(i)
		if maximum < int(i):
			maximum = int(i)
	range_ = maximum-minimum
	if curr <=1:
		print('Case '+str(k)+': '+str(minimum)+' '+str(maximum)+' 0')
	else:
		range_ = maximum - minimum
		print('Case '+str(k)+': '+str(minimum)+' '+str(maximum)+' '+str(range_))
	k+=1

