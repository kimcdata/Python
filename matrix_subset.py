# Python MAT2SIF converter#

# !/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Python functions for subsetting a matrix by a number of searchable criteria 

"""

from pandas import *

file_name = 'MuTHER_cis_results_chr11.txt'
file_name_out = 'outfile.txt'

comp = 'gt'

data = read_table(file_name, header = 0)

print(data.columns.values)

target = 'ZW10'

mask = data['Gene'].str.contains(target)
isnull = mask.isnull()

data_nonnull = data.loc[not isnull.any(),]

mask = data_nonnull['Gene'].str.contains(target)

data_target = data_nonnull.loc[mask,]

print(data_target)




# # # # # # try:
  # # # # # # opts, args = getopt.getopt(sys.argv[1:], "-i:-o:-t:-c:")
# # # # # # except getopt.GetoptError:
  # # # # # # print("mat2sif.py -i <inputfile> -o <outputfile> -h <headings> -t <search terms>")
  # # # # # # sys.exit("Command line syntax error")

# # # # # # for opt, arg in opts:
  # # # # # # if opt in ("-i"):
    # # # # # # file_name = arg
    # # # # # # print(file_name)
  # # # # # # if opt in ("-o"):
    # # # # # # file_name_out = arg
  # # # # # # if opt in ("-t"):
    # # # # # # terms = arg
  # # # # # # if opt in ("-h"):
    # # # # # # headings = arg

# # # # # # # open input file
# # # # # # cormat = open(file_name, 'r')
# # # # # # # open output file
# # # # # # outfile = open(file_name_out, 'w')

# # # # # # # open hub file
# # # # # # if hub_file_given:
  # # # # # # hub_file = open(hub_filename, 'r')
  # # # # # # hubs = []
  # # # # # # for line in hub_file:
    # # # # # # hubs.append(line.rstrip())

# # # # # # # create list of genes from first line of input file
# # # # # # colnames = cormat.readline().rstrip().split('\t')
# # # # # # colnames.pop(0)

# # # # # # seen = {}

# # # # # # t0 = time.clock()

# # # # # # for line in cormat:
  # # # # # # currLine = line.rstrip().split('\t')
  # # # # # # rowLab = currLine[0]
  # # # # # # print("rowLab " + rowLab)
  # # # # # # if hub_file_given:
    # # # # # # if rowLab in hubs:
      # # # # # # print("hit")
      # # # # # # rowLabList = [currLine.pop(0)] * len(currLine)
      # # # # # # if comp in "gt":
        # # # # # # sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) >= thresh]
      # # # # # # elif comp in "lt":
        # # # # # # sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) <= thresh]
      # # # # # # else:
        # # # # # # sys.exit("gt/lt needed for -c")

      # # # # # # for x in sig:
        # # # # # # # print(x)
        # # # # # # key = "_".join(sorted(x[0:2]))
        # # # # # # # print(key)
        # # # # # # seq = "\t".join(x)
        # # # # # # if key not in seen:
          # # # # # # outfile.write(seq + "\n")
          # # # # # # seen[key] = 1
  # # # # # # if not hub_file_given:
    # # # # # # rowLabList = [currLine.pop(0)] * len(currLine)
    # # # # # # if comp in "gt":
      # # # # # # sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) >= thresh]
    # # # # # # elif comp in "lt":
      # # # # # # sig = [(i, j, k) for (i, j, k) in zip(rowLabList, colnames, currLine) if abs(float(k)) <= thresh]
    # # # # # # else:
      # # # # # # sys.exit("gt/lt needed for -c")

    # # # # # # for x in sig:
      # # # # # # # print(x)
      # # # # # # key = "_".join(sorted(x[0:2]))
      # # # # # # # print(key)
      # # # # # # seq = "\t".join(x)
      # # # # # # if key not in seen:
        # # # # # # outfile.write(seq + "\n")
        # # # # # # seen[key] = 1
# # # # # # outfile.close()
# # # # # # cormat.close()

# # # # # # t1 = time.clock()
# # # # # # print("t0: " + str(t0) + "\n")
# # # # # # print ("t1: " + str(t1) + "\n")
