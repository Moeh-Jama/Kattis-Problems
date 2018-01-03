number =input()
enter = []
for j in range(0, int(number)):
	e = input()
	enter.append(e)

for i in enter:
	if int(i)%400!=0:
		print(str(int((int(i)+ 400)/400)))
	else:
		print(int(int(i)/400))