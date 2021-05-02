# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 04:56:33 2020

@author: Rokas
"""

import numpy as np

# PRAEINA 20/21 TESTU

def mostFrequentDigits(a):
    
    values = []
    times = []
    
    a_to_string = ''.join(map(str,a))
    #aa_digits = list(a_to_string)
    #a_digits = list(map(int,aa_digits))
    a_digits = [int(i) for i in a_to_string]
    
    unique_val = list(set(a_digits))
    
    a_array = np.array(a_digits)
    
    for unique in unique_val:
        ind_times = np.where(a_array == unique )
        val_count = len(ind_times[0])
        values.append(unique)
        times.append(val_count)
    
    zipped = list(zip(values, times))
    zipped.sort(key = lambda index: index[1], reverse = True)
    
    if a != []:
        #unzipped
        unz_val, unz_times = zip(*zipped) # unzip function
        
        max_time = max(times)
        unz_times_arrays = np.array(unz_times)
        max_digit_ind = np.where(unz_times_arrays == max_time)
        max_times_num = len(max_digit_ind[0])
        
        return_digits_array = list(unz_val[:max_times_num])
    else:
        return_digits_array = []
    
    
      
    #print(f'unz_val: {unz_val} {unz_times}')
    #print(list(unz_val[:max_times_num]))
    
    return return_digits_array  #list(unz_val[:max_times_num])
    
    

