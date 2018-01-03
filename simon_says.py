test_cases = int(input())
for i in range(test_cases):
	response = input().split()
	if 'simon' in response and 'says' in response:
		#print(response[2:])
		string = ''
		for i in response[2:]:
			print(i, end=' ')
		print()
	else:
		print()