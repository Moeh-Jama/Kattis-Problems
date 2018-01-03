import sys

sentence = 'i cant sphhyttgk pig latin'.split()


def getPigVersion(sentence):
	n = ''
	#print(sentence)
	vowels = ['a','e','i','o','u', 'y']
	for i in sentence:
		if i[0].lower() in vowels:
			n+=i+'yay'
		else:
			j = 0
			x = i
			constants=[]
			string=''
			while j<len(x) and x[j].lower() not in vowels:
				constants.append(x[j])
				string+=x[j]
				j+=1
			if j<len(x):
				n+=x[j:]+str(string)+"ay"
			else:
				n+=str(string)
			#print(i[:j])
			n+=''
		n+=' '
	return n

for line in sys.stdin:
	print(getPigVersion(line.split()))
'''
words = ["the qhhhhck brlkewn fox","jumps over the lazy dog","and ordinary foxes","dont jump over lazy dogs"]
for i in words:
	print(getPigVersion(i.split()))'''