#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def count_chars_without_spaces(text):
    # Remove spaces from text
    text = text.replace(" ", "")
    length_stripped_text  = len(text)
    
    return length_stripped_text

def calculate_floor_and_ceiling(L):
    '''Returns a list of floor and ceiling of the square root of a number
    where floor is the first element and ceiling is the second element'''
    floor = math.floor(math.sqrt(L))
    ceil = math.ceil(math.sqrt(L))
    
    return [floor, ceil]

def determine_rows_and_colummns(floor_ceil_list, L):
    '''Returns a list with rows being the first element and columns the second'''
    floor = floor_ceil_list[0]
    ceil = floor_ceil_list[1]
    rows = 0
    columns = 0
    least_area = 0
    area = floor*ceil
    if (area)>=L:
        rows = floor
        columns = ceil
        
    else:
        # Increase floor by 1
        floor+=1
        rows = floor
        columns = ceil
        
    print(f"rows:{rows} column:{columns},")
        
    return [rows, columns]
        
def encryption(s):
    # Write your code here
    encrypted_string = ""
    L = count_chars_without_spaces(s)
    floor_ceil_list = calculate_floor_and_ceiling(L)
    rows_columns = determine_rows_and_colummns(floor_ceil_list, L)
    
    rows = rows_columns[0]
    columns = rows_columns[1]
    i = 0
    j = 0
    
    while i<columns:
        index = i
        
        # Loop as long as current index is last than or equal to last element index
        while index<=L-1:
            print(f"index:{index}")
            encrypted_string+=s[index]
            index+=columns
        encrypted_string+=" "
        i+=1
            
    
    return encrypted_string
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()