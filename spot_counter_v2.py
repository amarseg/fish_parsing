__author__ = 'am4613'

import os
import re
import csv
import pandas as pd

def spot_counter(folder):
    file_list = os.listdir(folder)
    file_list = [x for x in file_list if re.search('spots',x)]
    csvfile = open(folder + 'Results.txt','w')
    filewriter = csv.writer(csvfile, delimiter = '\t')
    filewriter.writerow(['Sample_Name']+['Cell'] +['Spots']+['Spots_data'])
    for j in range(0,len(file_list)):

        filename = file_list[j]
        cell_names = list()
        cell_spots = list()
        spots_data = list()
        spots = 0
        count = False
        save = False
        with open (folder + file_list[j],'r') as f:
            file_content = f.readlines()
        file_content.append('')
        for i in range(0,len(file_content)):
            if save = True
                spots_data.append(file_conten[i])
            if bool(re.search('CELL', file_content[i])):
                cell_names.append(file_content[i].split('\t')[1])
                count = False
                save = False
                cell_spots.append(spots - 3)
                spots = 0
            if bool(re.search('Y_POS',file_content[i])) and bool(re.search('SPOTS', file_content[i+1])):
                count = True
            if bool(re.search('Pos_Y', file_content[i])):
                save = True
            elif bool(re.search('Y_POS',file_content[i])) and not bool(re.search('SPOTS', file_content[i+1])):
                spots = 3
            if count:
                spots += 1
        if(spots ==3):
            cell_spots.append(0)
        else:
            cell_spots.append(spots - 4)
        for i in range(0,len(cell_names)):
                filewriter.writerow([filename] + [cell_names[i].rstrip()] + [str(cell_spots[i])]+[spots_data])


folder = "C:\\Users\\am4613\\Documents\\fish_parsing\\test"

spot_counter(folder)
