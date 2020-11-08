#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:06:32 2020

@author: hemma
"""
import math
import matplotlib.pyplot as plt
import numpy as np
import csv 

# data_path = 'IRIS.csv'

# class Iris():
#     def __init__(self, data_path, species):
#         self.data_path = data_path
#         self.species = species
#         self.header, self.data = self.extract_data()
#         self.ave_sepal_w = np.mean(self.data[:,1])
#         self.max_sepal_l = np.max(self.data[:,0])
        
#     def extract_data(self):
#         with open(self.data_path, 'r') as f:
#             reader = csv.reader(f, delimiter=',')
#             data = list(reader)
#             headings = data[0][:-1]
#             data = data[1:]
#             # data = [d for d in data if d[-1] == self.species]
#             # data = np.array([d[:-1] for d in data]).astype(float)
#             data = np.array([d[:-1] for d in data if d[-1] == self.species]).astype(float)
#             #data = np.array([d for d in data]).astype(float)
#             print (data)
#             return headings, data
        

# iris = Iris(data_path, 'Iris-setosa')  
# print(iris.data.shape)

  
data_path = 'Iris_Verginica.csv'

class Iris():
    def __init__(self, data_path):
        self.data_path = data_path
        #self.extract_data()
        self.header, self.data = self.extract_data()
        self.sepal_w = self.data[:,1]
        self.petal_l = self.data[:,2]
        self.ave_sepal_w = np.mean(self.data[:,1])
        self.max_sepal_l = np.max(self.data[:,0])
        
    def extract_data(self):
        with open(self.data_path, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            data = list(reader)
            headings = data[0]#[:-1]
            data = np.array(data[1:]).astype(float)
            print (data)
            return headings, data
        

iris_verginica = Iris(data_path)  
print(iris_verginica.ave_sepal_w)
# print(iris.data.shape)





data_path = 'Iris.csv'

class Iris_data(Iris):
    def __init__(self, data_path, species):
        self.species = species
        super().__init__(data_path)
        
        
    def extract_data(self):
        with open(self.data_path, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            data = list(reader)
            headings = data[0][:-1]
            data = data[1:]
            data = np.array([d[:-1] for d in data if d[-1] == self.species]).astype(float)
            print (data)
            return headings, data
        
iris_setosa = Iris_data(data_path, 'Iris-setosa')  
print(iris_setosa.ave_sepal_w)


plt.scatter(iris_setosa.sepal_w, iris_setosa.petal_l, label='setosa')
plt.scatter(iris_verginica.sepal_w, iris_verginica.petal_l, label='verginica')
plt.xlabel('sepal width')
plt.ylabel('petal length')
plt.legend(loc='center right')
