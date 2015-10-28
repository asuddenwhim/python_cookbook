class Bunch:
	def __init__(self, **arbs):
		self.__dict__.update(arbs)

def fun(x):
	point = Bunch(data=x, sq=x*x)
	if(point.sq > 4):
		print '...'
list = {1, 2, 3}

for n in list:
	fun(n)
