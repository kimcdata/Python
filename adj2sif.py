# Python Adjacency matrix to sif network format converter#

#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Python ADJ2SIF, take an adjacency file, such as output from Aracne, and convert to a 3-column sif file format with or without thresholding the edge score or gene symbol

-i input file name
-o output file name
-t absolute correlation threshold [all connections lower than this will not be written to the network file]
-h file containing target hub genes

~500000 values per second (22000 x 22000 adj file) (Saved for later comparisons to script improvements)

"""

import sys, getopt, time, csv, re
#import numpy, scipy, matplotlib


file_name = ''
hub_filename = ''
hub_file_given = False
file_name_out = 'outfile.txt'
thresh = 0

try:
	opts, args = getopt.getopt(sys.argv[1:], "-i:-o:-t:-h:")
except getopt.GetoptError:
	print("mat2sif.py -i <inputfile> -o <outputfile> -t <threshold> -h <hub_gene_file>")
	sys.exit("Command line syntax error")
	
for opt, arg in opts:
	if opt in ("-i"):
		file_name = arg
	elif opt in ("-o"):
		file_name_out = arg
	elif opt in ("-t"):
		thresh = float(arg)
	elif opt in ("-h"):
		hub_filename = arg
		hub_file_given = True
	
#open input file
adjfile = open(file_name, 'r')
#open output file
outfile = open(file_name_out, 'w')
#open hub file
if hub_file_given:
	hub_file = open(hub_filename, 'r')
	hubs = []
	for line in hub_file:
		hubs.append(line.rstrip())


seen = {}

t0 = time.clock()
print("STARTED PROCESSING")

for line in adjfile:
	
	currLine = line.rstrip().split('\t')
	#print(currLine)
	if not re.search('>',line):

		#get the first gene in the line
		gene_row = currLine.pop(0)
		
		#check if gene is hub gene
		if hub_file_given:
			print("HUBS:" + str(hubs))
			if gene_row in hubs:
				print('HIT')

				#get the next gene and every second item after that
				tar_genes = currLine[0:len(currLine):2]
				#print(len(tar_genes))
				row_lab_list = [gene_row] *len(tar_genes)

				#get the first value and every second item after that
				tar_gene_values = currLine[1:len(currLine):2]
				#print(len(tar_gene_values))

				#zip up the first gene, second genes and values if value > threshold
			
				sig = [(i,j,k) for (i,j,k) in zip(row_lab_list, tar_genes, tar_gene_values) if abs(float(k)) >= thresh ]

				#for each value
				for x in sig:
					#make a key
					key = "_".join(sorted(x[0:2]))
					#make the string to write to file
					seq = "\t".join(x)
					if key not in seen:
						outfile.write(seq + "\n")
						#add key to dictonary 'seen'
						seen[key] = 1

			

		if not hub_file_given:
			
			#get the next gene and every second item after that
			tar_genes = currLine[0:len(currLine):2]
			#print(len(tar_genes))
			row_lab_list = [gene_row] *len(tar_genes)

			#get the first value and every second item after that
			tar_gene_values = currLine[1:len(currLine):2]
			#print(len(tar_gene_values))

			#zip up the first gene, second genes and values if value > threshold
		
			sig = [(i,j,k) for (i,j,k) in zip(row_lab_list, tar_genes, tar_gene_values) if abs(float(k)) >= thresh ]

			#for each value
			for x in sig:
				#make a key
				key = "_".join(sorted(x[0:2]))
				#make the string to write to file
				seq = "\t".join(x)
				if key not in seen:
					outfile.write(seq + "\n")
					#add key to dictonary 'seen'
					seen[key] = 1
outfile.close()
adjfile.close()

t1 = time.clock()
print("END PROCESSING. TIME = " + str(t1-t0) + "s")

