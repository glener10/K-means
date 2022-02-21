try:
	from pylab import *
	from random import *
except ImportError as error:
	print("1. Install requirements:")
	print("  pip3 install --upgrade pip")
	print("  pip3 install -r requirements.txt ")
	print()
	exit(-1)

def readtable(name):
	f = open(name, 'r')
	lines = f.readlines()
	result = []
	for x in lines:
		result.append(x)
	f.close()
	tabela = []
	for x in range(0,len(result)):
		mydata=[_f for _f in (result[x].strip()).split(" ") if _f]
		if (mydata):
			tabela.append(mydata)
	return tabela


def column(matrix, i):
    return [float(row[i]) for row in matrix]
