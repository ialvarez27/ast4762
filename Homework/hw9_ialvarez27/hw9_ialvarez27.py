#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# Homework 9
# October 22, 2026


# In[1]:


import glob
import import_ipynb
from hw8_ialvarez27 import *
import gaussian as g


# In[2]:


# Code from P6

# Problem 1)
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


#Problem 2a)
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



#Problem 2b)
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


# In[3]:


print("Problem 2)")

# Stellar photometry:
photometry = np.array( [ # yguess, xguess, width, cy, cx, star, sky
# star 0
[ [   698,    512, np.nan, np.nan, np.nan, np.nan, np.nan],    # frame 0
[  np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],   # frame 1
[  np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]],  # frame 2
# star 1
[ [   668,    520, np.nan, np.nan, np.nan, np.nan, np.nan],   # frame 0
[  np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],   # frame 1
[  np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]],  # frame 2
# star 2
[ [   568,    283, np.nan, np.nan, np.nan, np.nan, np.nan],   # frame 0
[  np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],   # frame 1
[  np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]]   # frame 2
], dtype=float)

# Finding position of star 0 in other two frames
frame_1 = no_sky[1]
frame_2 = no_sky[2]

# Region based off frame 0 position
region_1 = frame_1[600:800, 400:600]
region_2 = frame_2[600:800, 400:600]

# Finding brightest pixel and converting to coordinates
position_1 = np.unravel_index(np.nanargmax(region_1), region_1.shape)
position_2 = np.unravel_index(np.nanargmax(region_2), region_2.shape)

# Finding coordinates
y1 = position_1[0] + 600
x1 = position_1[1] + 400

y2 = position_2[0] + 600
x2 = position_2[1] + 400

print(f"Frame 1: {y1, x1}")
print(f"Frame 2: {y2, x2}")


# In[14]:


print("Problem 1 continued)")
# Updating photometry array 
photometry[0, 1, :2] = [721, 566]
photometry[0, 2, :2] = [721, 566]

# Calculating the offsets 
offset_1 = photometry[0, 1, :2] - photometry[0, 0, :2]
offset_2 = photometry[0, 2, :2] - photometry[0, 0, :2] 

print(f"Offset_1: {offset_1}")
print(f"Offset_2: {offset_2}")

# Loop to calculate the other star's positions 
for i in range(1,3):
    photometry[i, 1, :2] =  photometry[i, 0, :2] + offset_1
    photometry[i, 2, :2] =  photometry[i, 0, :2] + offset_2

print(f"Positions of Star 1: {photometry[1, :, :2]}")
print(f"Positions of Star 2: {photometry[2, :, :2]}")


# In[17]:


print("Problem 3a)")

nstars, nframes, nparams = photometry.shape 

for i in range(nstars):
    for j in range(nframes):
        # Approx position
        yguess = int(photometry[i, j, 0])
        xguess = int(photometry[i, j, 1])

        # Selecting frame 
        frame = no_sky[j]

        # Create subimage
        y_start = yguess - 15
        x_start = xguess - 15
        subimage = frame[y_start : yguess+16, 
                         x_start : xguess+16].copy() 

        # Subtracting background light
        background = np.nanmedian(subimage)
        subimage = subimage - background

        # Inital Gaussian Parameters
        guess = ([3,3], [15,15], np.nanmax(subimage))

        # Fit Gaussian 
        width, center, height, err = g.fitgaussian(subimage,
                                                   guess = guess)
        # Average width
        avg_width = np.mean(np.abs(width))

        # Adding coordinates back 
        cy = center[0] + y_start
        cx = center[1] + x_start

        # Updating Photometry Table
        photometry[i, j, 2] = avg_width
        photometry[i, j, 3] = cy
        photometry[i, j, 4] = cx

        print(f"Star{i}, Frame {j}: width = {avg_width: .4f}, y = {cy:.4f}, x = {cx:.4f}")

# Photometry table: [[[6.98000000e+02 5.12000000e+02 1.00573556e+00 6.98576139e+02
                        # 5.12376728e+02            nan            nan]
                     # [7.21000000e+02 5.66000000e+02 4.10563900e-01 7.20701203e+02
                        # 5.65662641e+02            nan            nan]
                     # [7.21000000e+02 5.66000000e+02 3.54437475e-01 7.20567751e+02
                        # 5.65998853e+02            nan            nan]]

                     # [[6.68000000e+02 5.20000000e+02 1.06025758e+00 6.67872643e+02
                         # 5.20249469e+02            nan            nan]
                     # [6.91000000e+02 5.74000000e+02 1.63060605e+00 6.91927826e+02
                         # 5.66776411e+02            nan            nan]
                      # [6.91000000e+02 5.74000000e+02 5.05543705e+00 6.94439578e+02
                        # 5.76386394e+02            nan            nan]]

                      # [[5.68000000e+02 2.83000000e+02 1.05092334e+00 5.68265270e+02
                           # 2.83301751e+02            nan            nan]
                      # [5.91000000e+02 3.37000000e+02 3.73591328e+00 5.95479073e+02
                           # 3.33301080e+02            nan            nan]
                     # [5.91000000e+02 3.37000000e+02 2.53455284e+00 5.91456934e+02
                           # 3.36504585e+02            nan            nan]]]


# In[24]:


print("Problem 3b)")

# Average of all widths
mean_width = np.nanmean(photometry[:, :, 2])

# Aperture radius 
aperture_radius = 3 * mean_width

#Sky annulus radii
sky_inner = 5 * mean_width
sky_outer = 8 * mean_width 

# Subimage half-size 
subimage_halfsize = int(10 * mean_width)

print(f"Average width:      {mean_width: .4f}")
print(f"Aperture radius:    {aperture_radius: .4f}")
print(f"Inner sky radius:   {sky_inner: .4f}")
print(f"Outer sky radius:   {sky_outer: .4f}")
print(f"Subimage half-size: {subimage_halfsize: .4f}")

# The aperture radius is about 3 times the with to capture most of the star's light
# while not not including too much unnecessary background. 
# The sky annulus is about 5 to 8 times the width to measure the sky background
# while avoiding most of the star's light.
# The subimage half-size is about 10 times the width to ensure the entire 
# aperture and sky annulus are included.


# In[ ]:




