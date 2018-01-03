number = input()
sample = input()

result = 0

for i in sample.split():
	if int(i) < 0:
		result+=1

print(result)