__author__ = 'am4613'

import os
import re
import csv

def spot_counter(folder):
    file_list = os.listdir(folder)
    file_list = [x for x in file_list if re.search('spots',x)]
    csvfile = open(folder + 'Results.txt','w') 
    filewriter = csv.writer(csvfile, delimiter = '\t')
    filewriter.writerow(['Sample_Name']+['Cell'] +['Spots'])
    for j in range(0,len(file_list)):

        filename = file_list[j]
        cell_names = list()
        cell_spots = list()

        spots = 0
        count = False
        with open (folder + file_list[j],'r') as f:
            file_content = f.readlines()
        file_content.append('')
        for i in range(0,len(file_content)):
            if bool(re.search('CELL_START', file_content[i])):
                cell_names.append(file_content[i].split('\t')[1])
            if bool(re.search('SPOTS_START',file_content[i])):
                count = True
                spots = 0
            if bool(re.search('SPOTS_END', file_content[i])):
                count = False
                cell_spots.append(spots - 1)

            if count:
                spots += 1
        for i in range(0,len(cell_names)-1):
                filewriter.writerow([filename] + [cell_names[i].rstrip()] + [str(cell_spots[i])])


folder = "C:\\Users\\am4613\\OneDrive\\FISH\\Result\\"

spot_counter(folder)


