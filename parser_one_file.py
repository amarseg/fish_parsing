__author__ = 'am4613'

import os
import re
import csv
import pandas as pd
import numpy as np

file_name = "probes_data/new_data_spots.txt"

with open (file_name,'r') as f:
    file_content = f.readlines()

file_index = [i for i, s in enumerate(file_content) if 'FISH-QUANT' in s]
file_index.append(len(file_content))

master_df = pd.DataFrame()
for j in range(0, len(file_index)-1):
    infile = file_content[file_index[j]:file_index[j+1]]

    file_name_row = [i for i, s in enumerate(infile) if 'IMG_Raw' in s]
    file_name_df = infile[file_name_row[0]].split('\t')[1]


    cell_names_index = [i for i, s in enumerate(infile) if 'CELL' in s]
    cell_names_index.append(len(infile))
    column_name = infile[cell_names_index[1]+4].split('\t')
    for i in range(0,len(cell_names_index)-1):
        #Get all data for each dot in each cell, put in dataframe
        data = infile[cell_names_index[i]+5:cell_names_index[i+1]]
        if(cell_names_index[i]+5 - cell_names_index[i+1]-1 < 0):
            split_data = [row.split('\t') for row in data]
            cell_name = infile[cell_names_index[i]].split('\t')[1]
            reshaped_data = np.array(split_data).reshape(-1,31)
            df = pd.DataFrame(reshaped_data, columns = column_name)
            df['cell_name'] = cell_name.rstrip()
            df['file_name'] = file_name_df
            master_df = master_df.append(df, ignore_index = True)

master_df.to_csv('probes_data/Results.csv')
