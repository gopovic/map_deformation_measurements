# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:44:21 2017

@author: goran
"""
import argparse
import numpy
import os
import matplotlib.pyplot as plt


def get_error(ms_dist, gt_dist):
    #copy the rows of gt_dist to get the number of rows as in ms_dist    

    GT_dist=[]
    for i in range(numpy.shape(ms_dist)[1]):    # ms_dist has three dimensions, second dimension is the number of rows
        GT_dist.append(gt_dist)

    Error=[]
    for i in range(numpy.shape(ms_dist)[0]):
        Error.append(numpy.abs(numpy.subtract(ms_dist[i][:][:],GT_dist)))    # PROVJERI JOS
    return Error
    
    
def get_means_and_limits(dist_array):
    Means_array=[]
    Limits_array=[] 
         
    if len(numpy.shape(dist_array))==2:
        #only one algorithm is in the input
        nr_alg=1
        nr_rows=numpy.shape(dist_array)[0]
        nr_cols=numpy.shape(dist_array)[1]
    else:
        #multiple algorithms are in the input
        nr_alg=numpy.shape(dist_array)[0]
        nr_rows=numpy.shape(dist_array)[1]
        nr_cols=numpy.shape(dist_array)[2]
    
    # Means_array and Limits_array contain mean values and limits of all algorithms
    Means_array=[]
    Limits_array=[]
    # loop matrices of different algorithms
    for j in range(nr_alg):
        # for loop through matrix of measured distances
        matrix=numpy.asmatrix(dist_array[j][:][:])
        # means_array and limits_array contain mean values and limits for one algorithm
        means_array=[]
        limits_array=[]
        for i in range(nr_cols):
           column=matrix[:,i]
           mean=numpy.mean(column)
           dev=numpy.std(column,ddof=1)
           #for alpha=0.05
           limit=1.96*dev/numpy.sqrt(nr_rows)
           means_array.append(mean)
           limits_array.append(limit)           
        Means_array.append(means_array)
        Limits_array.append(limits_array)
    return Means_array, Limits_array        
    
   
def plot_data(Error_means, Error_limits, file_names, ticks_list):    
    if len(numpy.shape(Error_means))==1:
        #only one algorithm is in the input
        nr_rows=1
        nr_cols=numpy.shape(Error_means)
    else:
        nr_rows=numpy.shape(Error_means)[0]
        nr_cols=numpy.shape(Error_means)[1]
    
    ind=numpy.arange(nr_cols)
    width=0.75/nr_rows
    
    fig, ax=plt.subplots()
    
    rects=[]
    
    col_list=['b','r','y','g','m','c','orange','navy']
    for i in range(nr_rows):
        rect=ax.bar(ind+i*width, Error_means[i][:], width,color=col_list[i], yerr=Error_limits[i][:], error_kw=dict(ecolor='gray',lw=2), align='center')
        rects.append(rect)
    
    ax.set_ylabel('Error [m]')
    ax.set_title('')
    ticks=[]
    for i in range(len(ind)):
        ticks.append(ind[i]+width*(nr_rows-1)/2)
    ax.set_xticks(ticks)
    
    ax.set_xticklabels(ticks_list)
    
    plt.ylim(0)    
    ax.yaxis.grid(which="major")
    ax.legend(rects, file_names)
    ax.relim()
    ax.autoscale_view()
    plt.show()
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

    # Write data from csv in arguments into array     
    ms_dist=[]
    ticks_list=[]
    pom_ticks_list=[]
    for i in range(len(args.m)):
         pom=numpy.genfromtxt(args.m[i],dtype=str,delimiter=',')
         if len(pom_ticks_list)==0:
             pom_ticks_list=pom[0][:]
         else:
             pom_ticks_list=ticks_list
         ticks_list=pom[0][:]
         if not numpy.array_equal(ticks_list, pom_ticks_list):
             print 'WARNING:'
             print 'Ticks from different files do not match. Using the ticks from last the .csv in -m arguments'
         ms_dist.append(pom[1::][::])
                
                
    # check how many columns and rows do matrices have            
    if len(numpy.shape(ms_dist))==2:
        alg_num=1        
        row_num=numpy.shape(ms_dist)[0]
        col_num=numpy.shape(ms_dist)[1]
    else:
        alg_num=numpy.shape(ms_dist)[0]
        row_num=numpy.shape(ms_dist)[1]
        col_num=numpy.shape(ms_dist)[2]

    # convert matrix from string to float
    f_ms_dist=[]
    for i in range(alg_num):
        pom=[]        
        for j in range(row_num):        
            pom.append(map(float, ms_dist[i][j]))
        f_ms_dist.append(pom);
     
    ms_dist=f_ms_dist 
    gt_dist=numpy.genfromtxt(args.g[0],dtype=str,delimiter=',')
    
    
    gt_dist=map(float,gt_dist[1][::])

    for i in range(len(args.m)):
        if numpy.shape(ms_dist[i])[1]!=col_num or numpy.shape(ms_dist[i])[0]!=row_num:
            print 'ERROR:'
            print 'Mismatch of matrix dimensions between .csv files.'
            exit()
          
      
    if numpy.shape(gt_dist)[0]!=col_num:
        print 'ERROR:'
        print 'Mismatch between the measured and ground truth data in .csv files'
        exit()
        
    if len(numpy.shape(gt_dist))!=1:
        print 'ERROR:'
        print 'Too many rows in .csv file with ground truth.', len(gt_dist), 'found, but only 1 is required.'
        exit()
        
    Error=get_error(ms_dist,gt_dist)
    mal=get_means_and_limits(Error)

    # get file names from args
    names=[]
    for i in range(len(args.m)):
        names.append(os.path.splitext(args.m[i].name)[0])
        
    plot_data(mal[0][:][:], mal[1][:][:],names, ticks_list)
