#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# Homework 10
# November 6, 2026 


# In[2]:


import numpy as np
import import_ipynb
from hw9_ialvarez27 import *
from P7_ialvarez27.P6_ialvarez27_support_functions import *


# In[3]:


# Code from Practicum 7
def apphot(image, mask, radius, sky_radii, center):
    """
    Performs aperture photomtery on a target object.

    Parameters:
    -----------
    image: 2D numpy_like array
         The full astronomical image containing brightness pixel values
    mask: 2D numpy_like array
         Boolean array where True (1) represents good pixels and False (0) 
         represents bad pixels
    radius: float
        Radius of the star's photomtery aperture
    sky_radii: tuple of (float,float)
              Inner and outer sky annulus radii
    center: tuple of (float, float)
            Star's center coordinates (row, col)

    Returns:
    --------
    tuple: (stellar_flux, avg_sky, [optional] bad_pixels)
    """
    # Assigning to variables
    x , y = center 
    r_in, r_out = sky_radii

    # Creating sub-image boundaries 
    r = int(np.ceil(r_out))

    x_min = int(x) - r
    x_max = int(x) + r + 1

    y_min = int(y) - r
    y_max = int(y) + r +1

    # Extracting sky-image 
    sub_image = image[y_min : y_max, x_min :x_max]
    sub_mask  = mask [y_min : y_max, x_min :x_max]

    # Center coordinates relative to sub-image 
    sub_center = (y - y_min, x - x_min) # FIXED

    # Circular masks
    inner_disk = disk(r_in,  sub_center, sub_image.shape)
    outer_disk = disk(r_out, sub_center, sub_image.shape)

    # Selecting pixels in sky annulus 
    sky_annulus = outer_disk & ~inner_disk

    # Exclude bad pixels 
    good_sky = sky_annulus & sub_mask 

    # Average sky brightness
    avg_sky = np.mean(sub_image[good_sky])

    # Subtract background from the sub image
    sky_subtracted = sub_image - avg_sky

    # Making a mask for the photometry aperture
    aperture      = disk(radius, sub_center, sub_image.shape)
    good_aperture = aperture & sub_mask

    # Calculating total stellar flux 
    stellar_flux = np.sum(sky_subtracted[good_aperture])

    return stellar_flux, avg_sky

# Creating 21 x 21 image 
size  = 21
x0    = 10
y0    = 10
sigma = 2

# Generating coordinate arrays
y, x = np.indices((size, size))

# Creating a noiseless 2D Gaussian star
star = np.exp(-((x - x0)**2 + (y- y0)**2) / (2*sigma**2) )

# Mask where every pixel is good 
mask = np.ones((21, 21), dtype = bool)

# Run aperture photometry 
flux, sky = apphot(star, mask, 6, (7,10),(10,10))

print(f"Stellar Flux: {flux: .4f}")
print(f"Average Sky:  {sky: .4f}")


# In[8]:


print("Problem 2: Writing the function")

def dophot(table, cube, mask, radius, sky_radii):
    """
    Performs aperture photometry for each star in each frame. 

    Parameters:
    -----------
    table: astropy.table 
          Table containing target coordindates.
    cube: 3D numpy array_like
           3D array of the observational frames. 
    mask: numpy array_like
        An array identifying good and bad pixels.
    radius: float
         Radius of the photomtery aperture. 
    sky_radii: tuple of (float,float)
              Inner and outer sky annulus radii

    Returns:
    --------
    table: astropy.table
           Targeted coordinates that went through aperture photometry
    """
    # Make a copy of the original table 
    result = table.copy()

    # Loop through each star 
    for i in range(result.shape[0]):

        # Loop through each observational frame
        for j in range(result.shape[1]):
            y      = table [i, j, 3]
            x      = table [i, j, 4] 
            center = (x , y )       # Updated star center
            image  = cube[j, : , :] # Select correct 2D image

            # Peform aperture photometry
            stellar_flux, avg_sky = apphot(image, mask, radius,
                                           sky_radii, center)
            # Update photometry table 
            result[i, j, 5] = stellar_flux
            result[i, j, 6] = avg_sky
    return result



# In[7]:


print("Problem 3 Continued: ")

# Mask matching observational images
mask = np.all(np.isfinite(no_sky), axis=0)

# Using aperture and sky annulus radii values obtain from hw9
photometry_results = dophot(photometry, no_sky, mask, aperture_radius,(sky_inner, sky_outer))
print(photometry_results)

# Reshape pohotometry table into 2D
results_2d = photometry_results.reshape(9,7)

# Save results to an ASCII text file
np.savetxt("hw10_ialvarez27_problem2_photometry.txt", results_2d, fmt = "%.6f", 
           header = "yguess xguess width cy cx stellar_flux avg_sky")


# In[ ]:




