# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:17:03 2014

@author: max

Description: returnfield returns a magnetic or elecrical field 
vector. calcfield calculates the field

"""
from __future__ import division
import scipy as sc
import matplotlib as mp
import numpy as np

class Field:

    
    def __init__(self,f):
        
        """
            initalizes with a Function
            this feature will be implemented later
        """
        self.field = f;
    
    def returnField(self, r,t):
        
        """
            This Function returns the Force vector
            @r and the time t            
            
            
        """        
        
        
        return self.calcField(r,t);
        
        
    def calcField(self, r,t):
        """
            This Function Calculates the Force Vector
            on given r and time
        
        """
        
        return np.array([1,1,1])
        
        
    