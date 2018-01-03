streams ={
	'Audio':'0001',
	'Image':'0001',
	'Video':'0011',
	'Mixed': '0110'
}
Requests={
	'YouTube':['Audio', 'Video', 4],
	'Spotify':['Image', 'Audio', 2],
	'Facebook':['Image', 1]
}

def check(g):
	dec = 0
	for digit in g:
		dec = dec*2 + int(digit)
	return dec

print(check('111'))
#Home One asks for Video_Movie

def system_response(req):
	f = 'Audio'
	s = 'Mixed'
	get_total = check(streams[f]) + check(streams[s])
	#print(Requests[req][-1])
	if get_total < Requests[req][-1]:
		print('Data Lost')
	else:
		if s == 'Mixed':
			t = check(streams[f])
			need = check(streams[s]) - t
			if need - Requests[req][-1] >= 0:
				return bin(Requests[req][-1])[2:]
			
			

def request(user_request):
	result = system_response(user_request)
	total = check(streams[Requests[user_request][0]])
	total += check(streams[Requests[user_request][1]])
	print(result)
	if check(result) == total:
		print('launch successful')

request('YouTube')
