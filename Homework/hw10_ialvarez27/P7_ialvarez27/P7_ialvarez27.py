#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# Practicum 7
# October 28 2026 


# In[1]:


import numpy as np                               # load numerical module
from P6_ialvarez27_support_functions import disk #Function made from P6


# In[3]:


print("Problem 1: Writing a function")

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
    sub_center = (x - x_min, y - y_min)

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


# In[6]:


print("Problem 2: ")

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

# Based on the Total Flux formula: 2pi*(sigma**2), multiplied by the Rayleigh distribution
# 1-e^[-R**2 / 2 (sigma**2), the expected flux is around 24.85

# Expected sky background is a very small positive number since the Gaussian extends beyond
# the 6 pixel aperture, so some faint light reaches the annulus


# In[ ]:




