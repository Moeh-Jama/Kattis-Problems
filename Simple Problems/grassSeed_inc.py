cost=0
number_of_lawns = 0
total_cost = 0
i=0
cost = float(input())
number_of_lawns = input()
while i < int(number_of_lawns):
	en = input()
	total_cost += float(en.split()[0]) * float(en.split()[-1])
	i+=1
print(float(cost*total_cost))