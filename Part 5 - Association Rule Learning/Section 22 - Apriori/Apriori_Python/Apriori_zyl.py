#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 09:50:39 2019

@author: macintoshhd
"""

# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_optimisation.csv', header = None)
transactions = []
for i in range(0,7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0,20)])
    
# Training Apriori on the dataset
from apriori import apriori
rules = apriori(transactions, min_support =0.003, min_confidence =0.2, min_lift = 3, min_length =2)
#重点：定义参数


# Visualising the results
results = list(rules)
myResults = [list(x) for x in results]