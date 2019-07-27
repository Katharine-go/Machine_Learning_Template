#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 20:54:04 2019

@author: macintoshhd
"""

# Multiple Linear Regression

# Importing the libraries 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,4].values

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,3] = labelencoder_X.fit_transform(X[:,3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

# Avoiding the Dummy Variable Trap
#去除掉X的第0列
X = X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 0.2,random_state = 0)
                                                 
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.transform(y_train)"""            

# Fitting Multiple Linear Regression to the Training set
# 利用训练集创建回归器
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)    

# Predeicing the Test set Results
y_pred = regressor.predict(X_test)

# Building the optimal model using Backward Elimination
# 反向淘汰算法
import statsmodels.formula.api as sm
X_train = np.append(arr = np.ones((40,1)),values = X_train, axis = 1)
X_opt = X_train[:,[0,1,2,3,4,5]]   
# 选择自变量矩阵    
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
# 利用新导入的标准库建立回归模型，endog因变量，exdog自变量
regressor_OLS.summary()
# summary()查看回归器的相关信息，选择P_value最高的自变量，删除，再次进行相同的回归
X_opt = X_train[:,[0,1,3,4,5]]       
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train[:,[0,3,4,5]]       
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train[:,[0,3,5]]       
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()
X_opt = X_train[:,[0,3]]       
regressor_OLS = sm.OLS(endog = y_train, exog = X_opt).fit()
regressor_OLS.summary()