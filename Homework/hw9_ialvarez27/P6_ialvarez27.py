#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# Practicum 6
# October 21, 2026


# In[5]:


import numpy as np    # load numerical module
from astropy.io import fits
import glob
import import_ipynb
from hw8_ialvarez27 import *


# In[6]:


print("Problem 1) ")

def disk(radius, center, shape):
    """
    Finds the pixels in an image whose center is within a certain
    radius of a given position. 

    Parameters: 
    ----------
    radius: float
            The radius of the disk.
    center: tuple
            The center of the disk as (y,x)
    Shape: tuple
           The image shape as (y,x)

    Returns: 
    -------
    mask : 2D numpy array_like
           A boolean 2D mask array (True inside disk, False elsewhere)

    Example:
    -------
    >>> mask = disk(6.2, (12.3, 14.5), (25, 30))
    >>> mask[14,14]
    True 
    >>>mask[2,1]
    False

    """
    # Center coordinates 
    yc , xc = center

    # Creating an array of pixel coordinates 
    y , x   = np.indices(shape)

    # Boolean mask: checking if pixels are within radius
    mask = (x - xc)**2 + (y - yc)**2 <= radius**2

    return mask

# Calling function for required values 
disktest = disk(6.2, (12.3, 14.5), (25, 20))

# Storing the result in a fits file 
fits.writeto("disktest.fits", disktest.astype(np.uint8), overwrite = True)

# Print values of pixel indices [14,14] and [2,1]
print(f"Value at pixel [14,14]:   {disktest [14, 14]}")
print(f"Value at pixel [2,1]  :   {disktest [2,1]}")


# In[7]:


print("Problem 2a) Converting files from 2D to 3D")

# Find lamp_on files
lampon_files = sorted(glob.glob("hw6_data_export/rdpharocor_k_lampon*.fits"))

# Find lamp_off files
lampoff_files = sorted(glob.glob("hw6_data_export/rdpharocor_k_lampoff*.fits"))

# Check how many files were found
print(len(lampon_files))
print(len(lampoff_files))

# Create lamp_on cube

# Read first image
sample_on = fits.getdata(lampon_files[0])

# Create an empty 3D array 
lampon_cube = np.zeros((len(lampon_files), sample_on.shape[0], sample_on.shape[1])) 

# Fill the cube 
for i in range(len(lampon_files)):
    data = fits.getdata(lampon_files[i])
    lampon_cube[i, : , : ] = data 


# Create lamp_off cube

# Read first image
sample_off = fits.getdata(lampoff_files[0])

# Create an empty 3D array 
lampoff_cube = np.zeros((len(lampoff_files), sample_off.shape[0], sample_off.shape[1]))

# Fill the cube 
for i in range(len(lampoff_files)):
    data = fits.getdata(lampoff_files[i])
    lampoff_cube[i, : , : ] = data 


# In[8]:


print("Problem 2a)")

# Median Combine
median_on  = np.median(lampon_cube, axis = 0)
median_off = np.median(lampoff_cube, axis = 0)

# Subtraction 
flat_raw = median_on - median_off

# Normalize with region ((225, 225), (-225, -225))
sample = flat_raw[225 : -225, 225 : -225]

# Normalization factor 
norm_factor = np.median(sample)

# Normalize entire image 
flat = flat_raw / norm_factor

# Writting flat to fits file
fits.writeto("flat.flits", flat, overwrite = True)

# Printing pixel index [217, 184]
print(f" Value of [217, 184]: {flat[217,184]:.4f}")



# In[19]:


print("Problem 2b)")

# Creating a cube to store flat-corrected images 
flat_corrected = np.full_like(no_sky, np.nan, dtype = float)

# Identifying the pixels where division in valid
valid = np.isfinite(flat) & (flat != 0)

# Applying flat-field correction only to valid pixels
np.divide(no_sky, flat, out = flat_corrected, where = valid)

# Printing value of pixel index [217, 184] in each frame 
print(flat_corrected[ :, 217, 184])

# Selecting the last corrected frame
last_flatframe = flat_corrected[-1, : , : ]

# Getting the header from the last original object image
new_header = fits.getheader(datadir + objfile[-1] + ".fits").copy()

# Modifying the header
new_header["FLATCOR"] = (True, "Flat-field corrected")
new_header.add_history("Applied normalized flat-field correction")

# Saved the last corrected frame
fits.writeto("stars_13s_9_flat.fits", last_frame, header = new_header, overwrite = True)


# In[ ]:




