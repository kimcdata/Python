# Python MAT2SIF converter#

# !/usr/bin/env python

# -*- coding: utf-8 -*-

"""
Python functions for subsetting a matrix by a number of searchable criteria 

"""

import pandas as pd
import sys, getopt, argparse

class Args:
  pass
	
parser = argparse.ArgumentParser(description = 'Fetch column headings and search terms')
parser.add_argument('-c', nargs = '+')
parser.add_argument('-t', nargs = '+')
parser.add_argument('-i')
parser.add_argument('-o')
parser.parse_args(namespace=Args)


file_name = Args.i
outfile_name = Args.o
list_target_columns = Args.c
list_target_values = Args.t

tup_colvalue_pairs = zip(list_target_columns, list_target_values)

print(file_name)
print(outfile_name)
print(list_target_columns)
print(len(list_target_columns))
print(list_target_values)

data = pd.read_table(file_name, header = 0)
print(data.shape[0])
nrow = data.shape[0]

mask_store = []

for col, val in tup_colvalue_pairs:
	print(col)
	print(val)

	mask = data[col].str.contains(val)
	print(type(mask))
	mask[mask.isnull()] = False
	mask = mask.tolist()
	print(mask[:100])
	
	mask_store.append(list(mask))
	print(len(mask_store))

rows_towrite = []
	
for i in range(nrow):
	row_intersect = [l[i] for l in mask_store]
	hits = len([x for x in row_intersect if x])
	if(hits == len(list_target_columns)):
		rows_towrite.append(i)
		
if(len(rows_towrite) > 0):
	data_towrite = data.iloc[rows_towrite,:]
	data_towrite.to_csv(path_or_buf = outfile_name, sep = '\t')


