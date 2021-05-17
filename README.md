# K-means
Implementation carried out during the development of the Machine Learning course in the 5th Semester of Computer Science.

# Dependencies
To view the results quickly and practically, it is recommended to use the gnuplot tool:

sudo apt-get install gnuplot

# Instructions
To assist in the execution of the code we will have 2 auxiliary flags:

-c    Choose the number of clusters

-i    Choose the path of the input file (2 dimensions)

Example: ./python main.py -i ./data/input.dat -c 3


In this way, 4 files will be generated in the "clusters" folder, as follows:
- centros.dat
- output1.dat
- output2.dat
- output3.dat

To view the Clusters just use Gnuplot:

1- gnuplot

2- plot "centros.dat", "output1.dat", "output2.dat", "output3.dat"

<img src="/images/input_3c.png" alt="example"/>
