enter = input()
i = 0
sent = ''
while i < len(enter):
	if i>0 and enter[i] != enter[i-1]:
		sent+=enter[i]
	if i==0:
		sent+=enter[i]
	i+=1
print(sent)
