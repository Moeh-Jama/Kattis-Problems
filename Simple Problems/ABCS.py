first_line = input()
letters = input()
numbers = []
for i in first_line.split():
	numbers.append(i)
i = 0
minimum = numbers[0]
maximum = numbers[0]
while i < len(numbers):
	en = numbers[i]
	j = i
	if minimum > en:
		minimum = en
	elif maximum < en:
		maximum = en
	i+=1
i = 0
while i< len(numbers):
	if numbers[i] == minimum:
		numbers.pop(i)
		break
	i+=1
i = 0
while i< len(numbers):
	if numbers[i] == maximum:
		numbers.pop(i)
		break
	i+=1
mid = numbers[0]
dictionary = {}
dictionary['A'] = minimum
dictionary['B'] = mid
dictionary['C'] = maximum

for i in letters:
	print(dictionary[i], end=' ')