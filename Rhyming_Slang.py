
def checkIfCommonEndings(w, Rhym):
	if w.endswith(Rhym):
		return True

# Inputs
word = input()
num = int(input())


wordList = []
for i in range(num):
	response = input().split()
	for j in response:
		wordList.append(j)
word_endings = []
print(wordList)
for i in wordList:
	if checkIfCommonEndings(word, i):
		word_endings.append(i)
print(word_endings)
def testPhrases(word_endings, phrase):
	for i in word_endings:
		#print(i+' - '+str(phrase))
		if checkIfCommonEndings(i, phrase):
			return 'YES'
	return 'NO'


newNum = int(input())
phrases = []
for i in range(newNum):
	response = input()
	phrases.append(response)

for i in phrases:
	print(testPhrases(word_endings, i.split()[-1]))