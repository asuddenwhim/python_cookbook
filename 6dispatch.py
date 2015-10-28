#call a function according to keyword

words = ['cat', 'bear', 'dog']

def deal_with_cat():
	print 'meow'


def deal_with_bear():
	print 'grrr'


def deal_with_dog():
	print 'woof'

tokens = {'cat': deal_with_cat, 'bear': deal_with_bear, 'dog': deal_with_dog}


for word in words:
	callThisFunction = tokens[word]
	callThisFunction()
	print '---------------------------------------------------------------'