#map each key to multiple values

dic = {}

def addValues(key, list):
	for value in list:
		dic.setdefault(key, []).append(value)

tags = {'noun', 'verb', 'adjective'}
key = 'POS'

addValues(key, tags)

print dic