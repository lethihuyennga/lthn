# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:25:47 2024

@author: PC
"""

def tim_phan_tu_list_x(list,x):
    if x in list:
        return list.index(x)
    else:
        return None
list = [1,3,5,7,9,11]
if __name__=="__main__":
    print(tim_phan_tu_list_x(list,5))
    print(tim_phan_tu_list_x(list,10))