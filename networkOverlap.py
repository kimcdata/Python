#input: any number of network files in sif format with identical ID formats for points/nodes
#output: a new network file for each input network with only common edges remaining

# Python network merge (intersection)

#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Python network merge

-i input_file_names

"""
import sys, getopt, time, csv

fileoutsuffix = 'merge'

invar = sys.argv[1:]
print(invar)

first = 1

allSet = set()

for file in invar:

	netSet = set()
	net = open(file, 'r')
	
	for line in net:
		
		currLine = line.rstrip().split('\t')
		netSet.add(currLine[0])
		netSet.add(currLine[1])
	
	if first == 1:
		allSet.update(netSet)
		print('allset first', first, len(allSet))
	elif first == 0:
		allSet = allSet & netSet
		print('allset iter', first, len(allSet))
	first = 0
	#print(netSet)
	net.close()
	
#print('final: ',list(allSet))

for file in invar:

	net = open(file, 'r')
	outfilename = file + "_" + fileoutsuffix + ".txt"
	outnet = open(outfilename, 'w')
	
	for line in net:
		
		currLine = line.rstrip().split('\t')
		if (currLine[0] in allSet):
			if(currLine[1] in allSet):
				outnet.write("\t".join(currLine) + "\n")
	net.close()
	outnet.close()

sys.exit()
	
	
	
	
"""
for each argument passed to the function
	
	read in the network
	add the unique node IDs to a list

count the unique node IDs 

if the node has count == no. of input networks then the node should be kept


for each network
	writeLine to new file if both nodes have count == no. of input networks

"""

"""
try:
	opts, args = getopt.getopt(sys.argv[1:], "-i:")
except getopt.GetoptError:
	print("mat2sif.py -i <inputfiles> ")
	sys.exit("Command line syntax error")
	
for opt, arg in opts:
	if opt in ("-i"):
		file_names = arg
		
print(file_names)

#open input file
cormat = open(file_name, 'r')
#open output file
outfile = open(file_name_out, 'w')


#create list of genes from first line of input file
colnames = cormat.readline().rstrip().split('\t')
colnames.pop(0)

seen = {}

t0 = time.clock()

for line in cormat:

	currLine = line.rstrip().split('\t')
	rowLabList = [currLine.pop(0)]*len(currLine)
	if comp in "gt": 
		sig = [(i,j,k) for (i,j,k) in zip(rowLabList, colnames, currLine) if abs(float(k)) >= thresh ]
	elif comp in "lt":
		sig = [(i,j,k) for (i,j,k) in zip(rowLabList, colnames, currLine) if abs(float(k)) <= thresh ]
	else:
		sys.exit("gt/lt needed for -c")

	for x in sig:
		key = "_".join(sorted(x[0:2]))
		seq = "\t".join(x)
		if key not in seen:
			outfile.write(seq + "\n")
			seen[key] = 1

outfile.close()
cormat.close()

t1 = time.clock()
print("t0: " + str(t0) + "\n")
print ("t1: " + str(t1) + "\n")

"""



