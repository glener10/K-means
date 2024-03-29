<h1 align="center">K-means</h1>

<p align="center"> 🚀 Implementation carried out during the development of the Machine Learning course in the 5th Semester of Computer Science. </p>

Table of Contents

===================

<!--ts-->

- [Environment](#Environment)
- [Prerequisites](#Prerequisites)
- [Demo](#Demo)

<!--te-->

===================

# Environment

Execution environment used and tested:

**SO**: Ubuntu 20.04 **Kernel**: 5.8.0-63-generic

# Prerequisites

To view the results quickly and practically, it is recommended to use the gnuplot tool:

- [Gnuplot](http://www.gnuplot.info/)

```bash
#Install Gnuplot
$ sudo apt-get install gnuplot
```

# Demo

To assist in the execution of the code we will have 3 auxiliary flags:

**-c** :Choose the number of clusters

**-i** :Choose the path of the input file (2 dimensions)

**-o** :Choose the path of the output file

```bash
#Example
python3 main.py -i ./data/input.dat -c 3 -o ./clusters/
```

In this way, 4 files will be generated in the "clusters" folder, as follows:

- centers.dat
- cluster1.dat
- cluster2.dat
- cluster3.dat

To view the Clusters just use Gnuplot:

```bash
$ cd ./clusters/

$ gnuplot

$ plot "centers.dat", "output1.dat", "output2.dat", "output3.dat"
```

<img src="/images/input_3c.png" alt="example"/>
