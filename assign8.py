# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 19:20:13 2020

@author: RAM
"""




def outerfunction():
    ''' this function is supposed to have a nested
    function that checks whether the outerfunction has 
    a docstring size of more than 50 or not '''
    x = len(outerfunction.__doc__)
    def inner():
        if x > 50:
            print("Length of the docstring is more than 50")
        else:
            print("Length of the docstrig is less than equal to 50")
    return inner
    
fn =outerfunction()
fn()
