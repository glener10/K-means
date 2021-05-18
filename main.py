# (C) 2021 Glener Lanes Pizzolato


import numpy
from arquivos import *
import random
import argparse

NUMBER_CLUSTERS = 3
OUT_NAME = "./clusters/output"
INPUT_NAME = "./data/input.dat"


def d(x1,y1,x2,y2):
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))


def kmeans(data, NUMBER_CLUSTERS):
	x0=column(data,0)
	y0=column(data,1)

	out = [0] * (NUMBER_CLUSTERS+1)
	xM = [0] * (NUMBER_CLUSTERS)
	yM = [0] * (NUMBER_CLUSTERS)
	elements = [0] * NUMBER_CLUSTERS
	cluster = []

	tam_data = -1

	for i in range(0,NUMBER_CLUSTERS):
		elements[i] = 0
		aux_out = OUT_NAME + ("%d.dat"%(i+1))
		out[i] = open(aux_out,"wt")

	for i in range(0,len(x0)):
		aux = randint(0,NUMBER_CLUSTERS-1)
		cluster.append(aux)
		elements[cluster[tam_data]] = elements[cluster[tam_data]] +1
		tam_data = tam_data + 1
		#print cluster[i]

	change = 1
	while(change == 1):
		change = 0
		for i in range(0,NUMBER_CLUSTERS):
			xM[i] = 0.0
			yM[i] = 0.0
			for j in range(0,tam_data):
				if(cluster[j] == i):
					xM[i] = xM[i] + x0[j]
					yM[i] = yM[i] + y0[j]
			if(elements[i] > 0):
				xM[i] = xM[i] / elements[i]
				yM[i] = yM[i] / elements[i]

			else:
				xM[i]=0.0
				yM[i]=0.0

		for i in range(0,NUMBER_CLUSTERS):
			elements[i] = 0

		for j in range(0,tam_data):
			distance = d(x0[j],y0[j],xM[cluster[j]],yM[cluster[j]])
			for i in range(0,NUMBER_CLUSTERS):
				dist_current=d(x0[j],y0[j],xM[i],yM[i])
				if (dist_current < distance):
					distance = dist_current
					cluster[j] = i
					change = 1
				if(cluster[j] == i):
					elements[i] = elements[i] + 1	

	for i in range(0,tam_data):
		for k in range(0,NUMBER_CLUSTERS):
			if(cluster[i] == k):
				out[k].write("%f"%x0[i])
				out[k].write(" %f\n"%y0[i])

	out[NUMBER_CLUSTERS] = open("./clusters/centros.dat","wt")

	for i in range(0,NUMBER_CLUSTERS):
		out[NUMBER_CLUSTERS].write("%f "%xM[i])
		out[NUMBER_CLUSTERS].write("%f\n"%yM[i])

	for i in range(0,NUMBER_CLUSTERS):
		out[k].close()


def main():
	parser = argparse.ArgumentParser(description='K-means Implementation')
	parser.add_argument("--clusters", "-c", help="Number of Clusters", default=NUMBER_CLUSTERS, type=int)
	parser.add_argument("--input", "-i", help="Name of Input File", default=INPUT_NAME, type=str)
	args = parser.parse_args()

	data = readtable(args.input)

	kmeans(data,args.clusters)
main()

