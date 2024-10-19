# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:25:29 2024

@author: PC
"""

from random import randrange
n = randrange(-98,99)
def so_nguyen_ngau_nhien():
    if -99 <= n <= 98:
        if n < 2:
            return "Không phải là số nguyên tố"  
        for i in range(2, n):
            if n % i == 0:
                return "Không phải là số nguyên tố"
        return "Là số nguyên tố"  
    else:
        return "Số không hợp lệ"  
print(n,so_nguyen_ngau_nhien())