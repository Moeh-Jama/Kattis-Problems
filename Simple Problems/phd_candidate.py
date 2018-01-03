test_cases = int(input())
output = ""
i = 0
while i< test_cases:
	en = input()
	if '+' in list(en):
		addition = en.split('+')
		result = int(addition[0]) + int(addition[-1])
		output += str(result)+"\n"
	elif en.lower() == 'p=np':
		output+='skipped'+"\n"
	i+=1
print(output)