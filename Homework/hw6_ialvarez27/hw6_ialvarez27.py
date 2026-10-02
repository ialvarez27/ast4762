#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Isabella Alvarez
# HW 6
# October 1, 2026


# In[1]:


import numpy as np              # load numerical module
import astropy.io.fits as fits  # load FITS module
import os


# In[2]:


# P4 Code

# Defining Variables
datadir = "hw6_data_export/" # where to look for the files
fext    = ".fits" # identifies file extension

# Initializing 
objfile  = []
darkfile = []

# Populating lists 
files = sorted(os.listdir(datadir))

for file in files:
    if file.startswith("rdpharocor_stars_13s_"):
        objfile.append(file.removesuffix(fext))

    elif file.startswith("rdpharocor_dark_13s_"):
        darkfile.append(file.removesuffix(fext))

# Print statements
print(f"Data Directory: {datadir}")
print(f"FITS extension: {fext}")
print(f"Last element of objfile: {objfile[-1]}")
print(f"Last element of darkfile: {darkfile[-1]}")

# Reading one object image
image = fits.getdata( datadir + objfile[0] + fext)

# ny = rows, nx = columns
ny, nx = image.shape

print(f"Data Array size: {ny} , {nx}")

# Contain number of files
nobj  = len(objfile)
ndark = len(darkfile)

#Print statements
print(f"ny: {ny}")
print(f"nx: {nx}")
print(f"Number of files in objfile: {nobj}")
print(f"NUmber of files in darkfile: {ndark}")

# Creating 3D arrays
obj_cube  = np.zeros( (nobj, ny, nx),   dtype = np.float64)
dark_cube = np.zeros( (ndark, ny, nx), dtype = np.float64)

# Printing shape
print(f"Object cube shape: {obj_cube.shape}")
print(f"Dark cube shape:   {dark_cube.shape}")

# Target Data
for i in range (nobj):
    filename = datadir + objfile[i] + fext # location of a file
    data, objhead = fits.getdata(filename, header = True) # retrieves images pixel values and header
    obj_cube[ i, :, :] = data # copies the pixel values into a layer i, stored in the data cube

# Same code for dark data
for i in range (ndark):
    filename = datadir + darkfile[i] + fext 
    data, darkhead = fits.getdata(filename, header = True)
    dark_cube[ i, :, :] = data

# Printing observation date
print(f"Object observation date: {objhead["DATE-OBS"]}")
print(f"Dark observation date: {darkhead ["DATE-OBS"]}")


# In[3]:


print("Problem 2a): the function is np.median()")

# Want to calculate the median across the different images
# While keeping the rows and columns so axis = 0
# Code will be np.median(cube, axis = 0)


# In[4]:


print("Problem 2b) ")

# Calling the median combine function for dark data
med_dark = np.median(dark_cube, axis = 0) 

# Median-combined dark image of index [217, 184]
print(f" Pixel value at [217,184]: {med_dark[217, 184]}")


# In[5]:


print("Problem 2c): Adding a History Entry")

# Recording the dark data is now median-combined
darkhead.add_history("Median-combined dark frame")



# In[6]:


print("Problem 2d): Writing modified code to a file")

# Writing the modified header to a specific dark data file
fits.writeto("dark_13s_med.fits", med_dark, header = darkhead, 
             overwrite = True)


# In[7]:


print("Problem 2e):")

# Using broadcasting, which Numpy automatically performs with subtraction
corrected = obj_cube - med_dark

# Writing the first frame to hw6 file

    # Editing the header
firsthead = fits.getheader(datadir + objfile[0] + fext)
firsthead.add_history("Median dark subtracted")

fits.writeto("hw6_ialvarez27_prob2_graph1.fits", corrected[ 0, :, :], 
             header = firsthead, overwrite = True)

# Index value = [217, 184]
print(f"Value of pixel index before dark subtraction: {obj_cube [0, 217, 184]}")
print(f"Value of pixel index after dark subtraction: {corrected [0, 217, 184]}")

# Subtraction reflects it was subtracted from the median found in part b: 19.0


# In[ ]:




