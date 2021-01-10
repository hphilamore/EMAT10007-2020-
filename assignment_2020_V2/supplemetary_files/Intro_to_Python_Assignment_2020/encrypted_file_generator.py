#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:34:49 2020

@author: hemma
"""
import numpy as np
from os.path import exists
from funcs import *
import csv


file_path = 'douglas_data.txt'


with open(file_path, "r") as f:
        msg = f.read()
        print(msg)


output_data = encrypt(6, msg)
print(output_data)

with open('douglas_data_encrypted.txt', "w") as f:
        f.write(output_data)