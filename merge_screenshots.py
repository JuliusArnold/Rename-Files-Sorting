#!/usr/bin/env python
# coding: utf-8

import os 
import sys
import numpy as np
from numpy import sqrt, sin, cos, arcsin
import random 
import math as m
import datetime

from fpdf import FPDF
from tqdm import tqdm
from PIL import Image
#_____________________________________________________________________





path= "/home/julius/Pictures/"



def filter_pictures(list_pic):
    selected_screenshots = []

    for file in list_pic:
        ending = file.split('.')[-1]
        if ending == "png":
            if "Screenshot" in file:
                selected_screenshots.append(file)
        else: # If ending is not png
            pass
    
    return selected_screenshots

def select_menu(list_pic):
    print("Confirm to combine the following files:")
    print(": ")
    for file in list_pic:
        print(":",file)
    #
    q = input(" y /[n]:") 
    if q == "y" or q == "yes" or q == "Y" or q == "Yes":
        return True, list_pic
    else: 
        return False, []

def get_file_name():
    print(" Give Output Name:")
    return input(": :")

def combine_files(file_name,list_pic):

    cover = Image.open(path +list_pic[0])
    width,height = cover.size
    pdf = FPDF(unit="pt",format = [width,height])
    pdf.set_title(file_name)

    for image in tqdm(list_pic):
        pdf.add_page()
        img_path =  path + image
        pdf.image(img_path,0,0)
 
    pdf.output(file_name, "F")

def move_files(list_pic):
    combined = "combined_screenshots/"
    for file in list_pic:
        old_path = path+file
        new_path = path+combined+file
        os.rename(old_path,new_path)


# Main Function
def main():
    list_pic = sorted(os.listdir(path))
    filtered_screenshots = filter_pictures(list_pic)
    selected, selected_screenshots = select_menu(filtered_screenshots)
    file_name = get_file_name()
    if selected:
        combine_files(file_name,selected_screenshots)
        print(":",len(selected_screenshots),"were combined!")

        move_files(selected_screenshots)
        print(": Done!")



if __name__ == "__main__":
    main()
