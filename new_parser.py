__author__ = 'am4613'

import os
import re
import csv
import pandas as pd
import numpy as np

folder = "probes_data/"

file_list = os.listdir(folder)
file_list = [x for x in file_list if re.search('spots',x)]
master_df = pd.DataFrame()
for file in file_list:
    with open (folder + file,'r') as f:
        file_content = f.readlines()
    cell_names_index = [i for i, s in enumerate(file_content) if 'CELL' in s]
    cell_names_index.append(len(file_content))
    column_name = file_content[cell_names_index[1]+4].split('\t')
    for i in range(0,len(cell_names_index)-1):
        #Get all data for each dot in each cell, put in dataframe
        data = file_content[cell_names_index[i]+5:cell_names_index[i+1]]
        if(cell_names_index[i]+5 - cell_names_index[i+1]-1 < 0):
            split_data = [row.split('\t') for row in data]
            cell_name = file_content[cell_names_index[i]].split('\t')[1]
            reshaped_data = np.array(split_data).reshape(-1,31)
            df = pd.DataFrame(reshaped_data, columns =  column_name)
            df['cell_name'] = cell_name.rstrip()
            df['file_name'] = file
            master_df = master_df.append(df, ignore_index = True)

master_df.to_csv(folder + 'Results.csv')
