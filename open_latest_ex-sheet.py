#!/usr/bin/env python
# coding: utf-8

import os 
import sys
import numpy as np
from numpy import sqrt, sin, cos, arcsin
import random 
import math as m
import datetime

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import subprocess
#import pandas
#import pickle # save Data

# ML Package
#import tensorflow as tf
#import cv2 # Picture processing
#from sciann import Variable, Functional, SciModel, Parameter
#from sciann.constraints import Data, MinMax
#from sciann.utils.math import diff
#import sciann as sn
#_____________________________________________________________________



def main():
    wd = os.getcwd()
    #print(wd)
    
    pdfs = []
    list_wd = sorted(os.listdir(wd))
    for file in list_wd:
        if file.split('.')[-1] == "pdf":
            pdfs.append(file)
    #print(pdfs[-1])
    path = wd + "/" + pdfs[-1]
    #print(path)
    subprocess.call(["xdg-open",path])
    #open latest




if __name__ == "__main__":
    main()
