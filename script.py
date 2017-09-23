# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 20:40:00 2017


Script takes .csv file(s) with distances measured on the built map and .csv file with the ground truth distances.

.csv files in the arguments need to have same ticks in the first row and measurements in the following rows.

Number of measurements needs to be equal in all .csv files. In .csv file with ground truth only one row with
distances should be given.

For each distance given in .csv file the mean value from multiple measurements is calculated, along with the
(1-alpha) range

Data are stored in the "table" dictionary described below.

"table" shape
   key-> file (name of the .csv file)
   value ->  data  
               |  (ticks in graph)  |  (measurements from .csv) | (grount truth)  | mean error value |  1-alpha range
               -> ticks             |           meas            |       gt        |      err         |       lim
                                                 | (row from .csv)
                                                  --> meas_nr   
@author: goran
"""

import csv
import os
import matplotlib.pyplot as plt
import argparse
import numpy

def csv_read_measurements(table):
    for key in table:
        with open(key,'r') as csvfile:
            a=csv.reader(csvfile, delimiter=',')
            data=list(a)
            row_nr=len(data)
            for i in range(row_nr):
                if i==0:
                    table[key]['data']['ticks']=data[i]
                else:        
                    table[key]['data']['meas'][i]=data[i]

def csv_read_ground_truth(table, gt_csv):
    with open(gt_csv,'r') as csvfile:
        a=csv.reader(csvfile,delimiter=',')
        data=list(a)
        for key in table:
            table[key]['data']['gt']=data[1]

def get_error_and_limits(table):
    for key,data in table.iteritems():
        for column_number in range(len(data['data']['meas'][1])):
                err_column=[]
                for row_number in data['data']['meas']:
                    err=float(data['data']['meas'][row_number][column_number])-float(table[key]['data']['gt'][column_number])
                    err_column.append(err)
                err_column=numpy.abs(err_column)
                data['data']['err'].append(numpy.mean(err_column))
                data['data']['lim'].append(1.96*numpy.std(err_column,ddof=1)/numpy.sqrt(len(data['data']['meas'])))
    
def plot_data(table):
    
    column_number=len(table[table.keys()[1]]['data']['err'])
    ind=numpy.arange(column_number)
    width=0.75/len(table)
    fig,ax=plt.subplots()
    rects=[]
    col_list=['b','r','y','g','m','c','orange','navy']
    
    for i in range(len(table)):
        rect=ax.bar(ind+i*width, table[table.keys()[i]]['data']['err'], width,color=col_list[i], yerr=table[table.keys()[i]]['data']['lim'], error_kw=dict(ecolor='gray',lw=2), align='center')
        rects.append(rect)
    
    ax.set_ylabel('Error [m]')
    ax.set_title('')
    ticks=[]
    for i in range(len(ind)):
        ticks.append(ind[i]+width*(len(table)-1)/2)
    ax.set_xticks(ticks)
    print table[table.keys()[0]]['data']['ticks']
    ax.set_xticklabels(table[table.keys()[0]]['data']['ticks'])
    
    plt.ylim(0)    
    ax.yaxis.grid(which="major")
    
    #use csv names in legend    
    csv_names=[]
    for key in table:
        name=os.path.basename(key)
        name=os.path.splitext(name)[0]
        csv_names.append(name)
    ax.legend(rects, csv_names)
    ax.relim()
    ax.autoscale_view()
    plt.show()
    return

def check_data(table): 
    column_number=len(table[table.keys()[0]]['data']['meas'][1])
    for csv_file in table:
        for row in table[csv_file]['data']['meas']:
            if len(table[csv_file]['data']['meas'][row])!=column_number:
                print "Wrong number of measurements in", csv_file
                exit()
        if len(table[csv_file]['data']['gt'])!=column_number:
            print "Number of measurements and ground truth don't match (file", csv_file,")"
            exit()
    row_number=len(table[table.keys()[0]]['data']['meas']) 
    for csv_file in table:
        if len(table[csv_file]['data']['meas'])!=row_number:
            print "Wrong number of measurements in file:", csv_file
            exit()            
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Plots an error of the measured distances in a bar graph (comparison between multiple algorithms is possible). Each file with the measured distances requires the file with ground truth distances')
    parser.add_argument('-m', metavar='MEASURED_DISTANCES', required=True, nargs='+', type=argparse.FileType('r'), help='.csv with measured distances')
    parser.add_argument('-g', metavar='GROUND_TRUTH_DISTANCES',required=True, nargs=1, type=argparse.FileType('r'), help='.csv with ground truth distances')
    args=parser.parse_args()
    
    if len(args.g)>1:
        print 'ERROR:'
        print 'Multiple ground truth .csv files. Only one is needed for comparing the algorithms.'
        exit()
    
    #Initialize table
    table={}   
    files=[]
    for x in args.m:
        files.append(x.name)
        table[x.name]={'data':{'ticks':[],'meas':{},'gt':[],'err':[],'lim':[]}}
        
    csv_read_measurements(table)
    csv_read_ground_truth(table,args.g[0].name)
    check_data(table)
    get_error_and_limits(table)
    plot_data(table)
 
    