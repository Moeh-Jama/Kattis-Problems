alph = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
Alphabet_Array = []
dictionary = {}
og = {}
size = 0
for i in alph.split():
	Alphabet_Array.append(i)
	dictionary[i] = size
	og[i] = size
	size+=1
user_input = 'SGZVQBUQAFRWSLC'
key = 'ACM'
decript = 0

for i in dictionary:
	print(i + ', '+str(dictionary[i]))
j=0
saved = []
for i in user_input:
	if j<= len(key)-1:
		saved.append(Alphabet_Array[int(int(dictionary[i])-int(dictionary[key[j]]))%25])
		#print()
		j+=1
	#print(Alphabet_Array[(dictionary[i]+dictionary[key[1]])%25], end='')
i = len(key)
j = 0
print('-------------------')
for e in saved:
	print('\t\t\t\t'+e)
def min(a, b):
	#print(str(a)+ ', '+str(b))
	if a>b:
		return a-b
	else:
		return b-a
while i<len(user_input):
	#print(user_input[i]+', '+str(dictionary[user_input[i]])+'\t'+str(Alphabet_Array[dictionary[saved[j]]]), end=', ')
	#print(str(dictionary[saved[j]])+"\t"+str(Alphabet_Array[int(dictionary[user_input[i]]+dictionary[saved[j]])%25]))
	#print(user_input[i]+', '+str(saved[j])+', '+str(dictionary[saved[j]])+", "+str(dictionary[user_input[i]])+", "+str(min(int(dictionary[user_input[i]]),int(dictionary[saved[j]]))%25)+', '+str(Alphabet_Array[int(int(dictionary[user_input[i]])-int(dictionary[saved[j]]))%25]))
	#print(Alphabet_Array[int(int(dictionary[Alphabet_Array[i]])-int(dictionary[saved[j]]))%25])
	if int(dictionary[user_input[i]]) < int(dictionary[saved[j]]):
		print(user_input[i]+', '+str(dictionary[user_input[i]])+'\t'+str(Alphabet_Array[dictionary[saved[j]]]), end=', ')
		print(str(dictionary[saved[j]])+"\t"+str(Alphabet_Array[int(dictionary[user_input[i]]+dictionary[saved[j]])%25]))
		#print(Alphabet_Array[int(int(dictionary[user_input[i]])+int(dictionary[saved[j]]))%25])
		if Alphabet_Array[int(int(dictionary[user_input[i]])+int(dictionary[saved[j]]))%25] in saved:
			saved.append(Alphabet_Array[int((int(dictionary[user_input[i]])+int(dictionary[saved[j]]))+2)%25])
		else:
			saved.append(Alphabet_Array[int(int(dictionary[user_input[i]])+int(dictionary[saved[j]]))%25])
	else:
		print(user_input[i]+', '+str(dictionary[user_input[i]])+'\t'+str(Alphabet_Array[dictionary[saved[j]]]), end=', ')
		print(str(dictionary[saved[j]])+"\t"+str(Alphabet_Array[int(dictionary[user_input[i]]-dictionary[saved[j]])%25]))
		#print(Alphabet_Array[int(int(dictionary[user_input[i]])-int(dictionary[saved[j]]))%25])
		if Alphabet_Array[int((int(dictionary[user_input[i]])-int(dictionary[saved[j]])))%25] in saved:
			
			saved.append(Alphabet_Array[int(int(dictionary[user_input[i]])-int(dictionary[saved[j]])+2)%25])
		else:
			saved.append(Alphabet_Array[int(int(dictionary[user_input[i]])-int(dictionary[saved[j]]))%25])
	j+=1
	i+=1

print((int(21-18)%25))