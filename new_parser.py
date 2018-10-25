__author__ = 'am4613'

import os
import re
import csv
import pandas as pd

folder = "test_data/"

file_list = os.listdir(folder)
file_list = [x for x in file_list if re.search('spots',x)]

for file in file_list:
    with open (folder + file,'r') as f:
        file_content = f.readlines()
    cell_names_index = [i for i, s in enumerate(file_content) if 'CELL' in s]
    for i in cell_names_index:
        #Get all data for each dot in each cell, put in dataframe
        data = file_content[cell_names_index[i]+5:cell_names_index[i+1]-1] 




csvfile = open(folder + 'Results.txt','w')
filewriter = csv.writer(csvfile, delimiter = '\t')
filewriter.writerow(['Sample_Name']+['Cell'] +['Spots']+['Spots_data'])
