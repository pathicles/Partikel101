# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 16:29:15 2014

@author: max
"""

from __future__ import division
import matplotlib.pyplot as plt

class Drawer:
    
    
     
    
    def __init__(self,r):
    
        self.r = r;
        
    def Draw(self):
        """        
        Draws the calculated trajectory
        
        
        """
        
        fig = plt.figure();
        ax = fig.gca(projection='3d')
        
        x = [];
        y = [];
        z = [];        
        
        
        for i in self.r:
            
            x.append(i[0]);
            y.append(i[1]);
            z.append(i[2]);
                      
        #ax = fig.gca(projection='3d');
        ax.plot(x,y,z,label = 'Tajectory');
        ax.legend();
        plt.show()
            
            
        