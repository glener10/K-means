from pylab import *
from random import *

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

def grafico( a ):
	y=list(range(0,size(a)))
	plot (y,a,"ro")
	xlabel('SAMPLE')
	ylabel('DATA')
	show()

def writefile(name,array):
	f = open(name, 'w')
	for item in array:
		f.write(str(item)+"\n")
	f.close()

def column(matrix, i):
    return [float(row[i]) for row in matrix]
