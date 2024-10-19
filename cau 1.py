# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 15:14:03 2024

@author: PC
"""
def kiem_tra_chuoi_palindrome(chuoi): 
    if chuoi== str(chuoi)[::-1]:
        return "đây là chuoi palindrome "
    return"đây không là chuỗi palindrome"
if __name__=="__main__":
    print("hello", kiem_tra_chuoi_palindrome("hello"))
    print("madam", kiem_tra_chuoi_palindrome("madam"))