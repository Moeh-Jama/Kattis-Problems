rows = int(input())

winner_without_CD=0
for i in range(0, rows):
	s = input()
	if 'CD' not in s:
		winner_without_CD+=1

print(winner_without_CD)