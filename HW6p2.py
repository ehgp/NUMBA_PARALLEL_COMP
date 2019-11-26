# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:58:21 2019

@author: egarcia2
"""
import numpy as np
import matplotlib.pyplot as plt 
import random
def dice(n):
    rolls = []
    fair_rolls = []
    biased_rolls = []
    for i in range(n):
        loaded_die = random.choices([1,2,3,4,5,6], [0.15, 0.15, 0.15, 0.15, 0.15, 0.25])
        two_dice = random.randint(1, 6) + loaded_die[0]
        fair_die = two_dice - loaded_die[0]
        biased_die = loaded_die[0]
        rolls.append(two_dice)
        fair_rolls.append(fair_die)
        biased_rolls.append(biased_die)
    return plt.hist(rolls, bins=np.arange(1+1, 12+2)-0.5), plt.title('two dice rolls'), plt.figure(), plt.hist(fair_rolls, bins=np.arange(1, 6+2)-.5), plt.title('fair die rolls'),plt.figure(), plt.hist(biased_rolls, bins=np.arange(1, 6+2)-.5), plt.title('biased die rolls')
           
n1 = input("How many times will you roll?: ")
n1 = int(n1)
dice(n1)