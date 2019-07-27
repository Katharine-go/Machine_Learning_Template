#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 20:33:17 2019

@author: macintoshhd
"""

#Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
# X:包含自变量向量矩阵 iloc:取数据集中的某些行和列，[行，列]，:表示取所有行，:-1表示不取最后一列
# 现在X的类型是object无法查看
y = dataset.iloc[:,1].values
# y:代表因变量的向量

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X, y, test_size = 1/3,random_state = 0)
# random_state:测试集中随机选择的方式

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.transform(y_train)"""

# Fitting Simple Linear Regression to the Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Visualising the training set results
plt.scatter(X_train,y_train,color = 'red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
# plot画直线 代表线性回归的直线
plt.title('salary VS Experience(training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the training set results
plt.scatter(X_test,y_test,color = 'red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
# plot画直线  不把X_train替换成X_test，因为线性回归是用训练集创建的
plt.title('salary VS Experience(test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


