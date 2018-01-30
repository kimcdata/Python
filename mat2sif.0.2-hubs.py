# Python MAT2SIF converter#

# !/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Python MAT2SIF, take a square correlation matrix and convert to a 3-column sif file format with or without thresholding the correlation value

-i input_file_name
-o output_file_name
-t absolute_correlation_threshold [all connections lower than this will not be written to the network file]
-c comparison to make (greater than or less than)
-h hub file
~266000 values per second (10781 x 10781 square matrix) (Saved for later comparisons to script improvements)

"""

import sys, getopt, time, csv

# import numpy as np


file_name = ''
file_name_out = 'outfile.txt'
thresh = 0
comp = 'gt'
hubs = []
hub_filename = ''
hub_file_given = False

try:
  opts, args = getopt.getopt(sys.argv[1:], "-i:-o:-t:-c:-h:")
except getopt.GetoptError:
  print("mat2sif.py -i <inputfile> -o <outputfile> -t <threshold>")
  sys.exit("Command line syntax error")

for opt, arg in opts:
  if opt in ("-i"):
    file_name = arg
    print(file_name)
  if opt in ("-o"):
    file_name_out = arg
  if opt in ("-t"):
    thresh = float(arg)
  if opt in ("-c"):
    comp = arg
  if opt in ("-h"):
    hub_filename = arg
    print(hub_filename)
    hub_file_given = True

# open input file
cormat = open(file_name, 'r')
# open output file
outfile = open(file_name_out, 'w')

# open hub file
if hub_file_given:
  hub_file = open(hub_filename, 'r')
  hubs = []
  for line in hub_file:
    hubs.append(line.rstrip())

# create list of genes from first line of input file
colnames = cormat.readline().rstrip().split('\t')
colnames.pop(0)

seen = {}

t0 = time.clock()

for line in cormat:
  currLine = line.rstrip().split('\t')
  rowLab = currLine[0]
  print("rowLab " + rowLab)
  if hub_file_given:
    if rowLab in hubs:
      print("hit")
      rowLabList = [currLine.pop(0)] * len(currLine)
      if comp in "gt":
        sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) >= thresh]
      elif comp in "lt":
        sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) <= thresh]
      else:
        sys.exit("gt/lt needed for -c")

      for x in sig:
        # print(x)
        key = "_".join(sorted(x[0:2]))
        # print(key)
        seq = "\t".join(x)
        if key not in seen:
          outfile.write(seq + "\n")
          seen[key] = 1
  if not hub_file_given:
    rowLabList = [currLine.pop(0)] * len(currLine)
    if comp in "gt":
      sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) >= thresh]
    elif comp in "lt":
      sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) <= thresh]
    else:
      sys.exit("gt/lt needed for -c")

    for x in sig:
      # print(x)
      key = "_".join(sorted(x[0:2]))
      # print(key)
      seq = "\t".join(x)
      if key not in seen:
        outfile.write(seq + "\n")
        seen[key] = 1
outfile.close()
cormat.close()

t1 = time.clock()
print("t0: " + str(t0) + "\n")
print ("t1: " + str(t1) + "\n")
