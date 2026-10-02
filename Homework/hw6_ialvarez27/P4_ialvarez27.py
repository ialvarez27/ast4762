#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# P4
# October 1, 2026


# In[1]:


import numpy as np              # load numerical module
import astropy.io.fits as fits  # load FITS module
import os


# In[3]:


print ("Problem 2a): Defining Variables")

# Defining Variables
datadir = "hw6_data_export/" # where to look for the files
fext    = ".fits" # identifies file extension


# In[5]:


print ("Problem 2b): Initializing and Populating 2 lists ")

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


# In[6]:


print("Problem 2c):")

print(f"Data Directory: {datadir}")
print(f"FITS extension: {fext}")
print(f"Last element of objfile: {objfile[-1]}")
print(f"Last element of darkfile: {darkfile[-1]}")


# In[7]:


print("Problem 2d):")

# Reading one object image
image = fits.getdata( datadir + objfile[0] + fext)

# ny = rows, nx = columns
ny, nx = image.shape

print(f"Data Array size: {ny} , {nx}")


# In[8]:


print("Problem 2e):")

# Contain number of files
nobj  = len(objfile)
ndark = len(darkfile)

#Print statements
print(f"ny: {ny}")
print(f"nx: {nx}")
print(f"Number of files in objfile: {nobj}")
print(f"NUmber of files in darkfile: {ndark}")

# Why not hardcode them?
"""
If you hardcode, any files that are added or deleted will not update in the code.
Setting the variables equal to the length of the folder will automatically adjust
to any changes in the number of files.
"""


# In[9]:


print("Problem 3a):")

# Creating 3D arrays
obj_cube  = np.zeros( (nobj, ny, nx),   dtype = np.float64)
dark_cube = np.zeros( (ndark, ny, nx), dtype = np.float64)

# Printing shape
print(f"Object cube shape: {obj_cube.shape}")
print(f"Dark cube shape:   {dark_cube.shape}")


# In[10]:


print("Problem 3b):")

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

# Why not print TIME-OBS?

"""
TIME-OBS is already included in DATE_OBS in modern FITS files, so it is unecessary.

"""


# In[ ]:




