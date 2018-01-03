s = """a

@

at symbol

n

[]\[]

brackets, backslash, brackets

b

8

digit eight

o

0

digit zero

c

(

open parenthesis

p

|D

bar, capital D

d

|)

bar, close parenthesis

q

(,)

parenthesis, comma, parenthesis

e

3

digit three

r

|Z

bar, capital Z

f

#

number sign (hash)

s

$

dollar sign

g

6

digit six

t

']['

quote, brackets, quote

h

[-]

bracket, hyphen, bracket

u

|_|

bar, underscore, bar

i

|

bar

v

\/

backslash, forward slash

j

_|

underscore, bar

w

\/\/

four slashes

k

|<

bar, less than

x

}{

curly braces

l

1

digit one

y

`/

backtick, forward slash

m

[]\/[]

brackets, slashes, brackets

z

2

digit two"""
k=0
top = []
bot = []
english={}
t = ''
for i in s.split("\n"):
	if i !='':
		if k==0:
			top.append(i)
		elif k==1:
			bot.append(i)
		k=(k+1)%3

i = 0
while i < len(top):
	english[top[i]] = bot[i]
	i+=1
english[' ']=' '
string = input().lower()
result = ''
for i in string:
	if i in english:
		print(english[i], end='')
	else:
		print(i, end='')