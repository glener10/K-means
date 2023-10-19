#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'All'
__email__ = '{glenerpizzolato}, @gmail.com'
#__version__ = '{1}.{0}.{0}'

try:
	from files import *
	import argparse
except ImportError as error:
	print("1. Install requirements:")
	print("  pip3 install --upgrade pip")
	print("  pip3 install -r requirements.txt ")
	print("2. Install Gnuplot:")
	print("  sudo apt-get install gnuplot")
	print()
	exit(-1)

DEFAULT_CLUSTERS = 3
DEFAULT_OUTPUT = "./clusters/"
DEFAULT_INPUT = "./data/input.dat"


def d(x1,y1,x2,y2):
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))

def kmeans(data, cluster_number,output):
	x0=column(data,0)
	y0=column(data,1)

	out = [0] * (cluster_number+1)
	xM = [0] * (cluster_number)
	yM = [0] * (cluster_number)
	elements = [0] * cluster_number
	cluster = []

	data_size = -1

	for i in range(0,cluster_number):
		elements[i] = 0
		aux_out = output + ("cluster%d.dat"%(i+1))
		out[i] = open(aux_out,"wt")

	for i in range(0,len(x0)):
		aux = randint(0,cluster_number-1)
		cluster.append(aux)
		elements[cluster[data_size]] = elements[cluster[data_size]] +1
		data_size = data_size + 1
		#print cluster[i]

	change = 1
	while(change == 1):
		change = 0
		for i in range(0,cluster_number):
			xM[i] = 0.0
			yM[i] = 0.0
			for j in range(0,data_size):
				if(cluster[j] == i):
					xM[i] = xM[i] + x0[j]
					yM[i] = yM[i] + y0[j]
			if(elements[i] > 0):
				xM[i] = xM[i] / elements[i]
				yM[i] = yM[i] / elements[i]

			else:
				xM[i]=0.0
				yM[i]=0.0

		for i in range(0,cluster_number):
			elements[i] = 0

		for j in range(0,data_size):
			distance = d(x0[j],y0[j],xM[cluster[j]],yM[cluster[j]])
			for i in range(0,cluster_number):
				dist_current=d(x0[j],y0[j],xM[i],yM[i])
				if (dist_current < distance):
					distance = dist_current
					cluster[j] = i
					change = 1
				if(cluster[j] == i):
					elements[i] = elements[i] + 1	

	for i in range(0,data_size):
		for k in range(0,cluster_number):
			if(cluster[i] == k):
				out[k].write("%f"%x0[i])
				out[k].write(" %f\n"%y0[i])

	out[cluster_number] = open("%s/centers.dat"%(output),"wt")

	for i in range(0,cluster_number):
		out[cluster_number].write("%f "%xM[i])
		out[cluster_number].write("%f\n"%yM[i])

	print("To plot the graph run the commands:")
	print()
	print("$ cd %s"%(output))
	print("$ gnuplot")
	print("$ plot 'centers.dat'", end="")

	for i in range(0,cluster_number):
		out[k].close()
		print(", 'cluster%d.dat'"%(i+1), end="")

	print("\n\nto finish run:\n$ exit")
	print()
		

def add_arguments(parser):
	parser.add_argument("--clusters", "-c", help="Number of Clusters", default=DEFAULT_CLUSTERS, type=int)
	parser.add_argument("--input", "-i", help="Path to input File", default=DEFAULT_INPUT, type=str)
	parser.add_argument("--output", "-o", help="Path to output File", default=DEFAULT_OUTPUT, type=str)
	return parser

def main():
	parser = argparse.ArgumentParser(description='K-means')
	parser = add_arguments(parser)
	args = parser.parse_args()

	data = readtable(args.input)
	kmeans(data,args.clusters,args.output)

if __name__ == '__main__':
	exit(main())