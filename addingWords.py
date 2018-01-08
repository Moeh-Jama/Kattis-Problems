import sys
definedTerms = {}

def WordCalculation(Word_Equation, Terms):
	sign = '+'
	WordCountTotal = 0
	operators = ['+','-']
	for i in Word_Equation:
		# Check if i not a defined term
		if i not in Terms and i not in operators:
			# If the term is not defined return False.
			return False
		elif i in operators:
			sign = i
		elif i in Terms:
			# add or subtract Term i depending on the
			# sign before it.
			if sign=='+':
				WordCountTotal+=Terms[i]
			elif sign=='-':
				WordCountTotal-=Terms[i]
	return int(WordCountTotal)


for line in sys.stdin:
	#print(definedTerms)
	response = line
	if response=='clear':
		# The dictionary definedTerms is cleared of all
		# its contents.
		definedTerms.clear()
	else:
		ArriedString = line.split()
		if ArriedString[0]=='def':
			# Defining the new varibale into our dictionary.
			# I assume that all defining will contain at maximum
			# 3 elements in the line.
			definedTerms[ArriedString[1]] = int(ArriedString[2])
		elif ArriedString[0] == 'calc':
			functionResponse = WordCalculation(ArriedString[1:-1], definedTerms)
			known = False
			# if functionalResponse does not return a False then
			# check if there is a Term that has the 
			# same value as functionResponse!
			if functionResponse != False:
				for i in definedTerms:
					if definedTerms[i] == functionResponse:
						known = True
						print((response[5:-1]+' '+i))
						break
			# If known is false then the product value 
			# does not have a term the equals it, so we
			# print unknown.
			if known==False:
				print((response[5:-1]+' '+'unknown'))
