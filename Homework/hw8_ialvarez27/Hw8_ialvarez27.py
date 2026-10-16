#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# Hw 8
# October 15, 2026


# In[1]:


import numpy as np              # load numerical module
import astropy.io.fits as fits  # load FITS module
import import_ipynb
from hw6_ialvarez27 import *


# In[2]:


# Code from P5 
def normmedcomb(data, region = None):
    """
    Normalize each image and median-combine the stack.

    Parameters:
    -----------
    data : 3D numpy array_like
           An array of data that contains dark-subtracted
           sky flux (frames, y, x).
    region: tuple, optional
            Contians corner coordinates((y1, x1), (y2, x2))
            Default: the whole image.

    Returns: 
    --------
    combined: 2D numpy array_like
              The normalized, median-combined image.
    norm_factors: 1D numpy array_like
              Containing the normalized factors for each frame
    """

    # Copy of original input data
    normdata = data.copy()

    # Create an array to store normalized factors
    norm_factors = np.zeros(data.shape[0]) 

    # Loop through each image 
    for i in range(data.shape[0]):

        # Normalized region
        if region is None: 
            sample = data [i, : , : ] #entire 2D frame
        else:
            (y1, x1), (y2, x2) = region # extract coordinates
            sample = data[i, y1 : y2, x1 : x2] 

        # Find the median
        norm_factors [i] = np.median(sample)

        # Normalize the image
        normdata[i, : , :] = (data[i, : , : ]) / norm_factors[i]

        # Median-combine normalized frames 
        combined = np.median(normdata, axis = 0)

    return combined, norm_factors 

# Defining normalization region
sky_region = ((225, 225), (-225, -225))

# Setting the normalized and median-combined sky images to variables
sky_mednorm, sky_factors = normmedcomb(corrected, region = sky_region)

# The noramlization factors: 10864. 11057. 10536. 
#  10559. 11046. 10623.  9916.  9916.  9859.


# In[3]:


print("Problem 2) Writing the function")

def skycormednorm(obj, sky, region = None):
    """
    Subtract a de-normalized sky from a dark-subtracted
    object frame. 

    Parameters:
    -----------
    obj: 2d numpy array_like 
        Dark-subtracted object frame
    sky: 2d numpy array_like
        Normalized sky frame 
    region: tuple, optional
        ((y1, x1) (y2, x2))
        Defualt is the whole frame 

    Returns: 
    --------
    sky_subtracted: 2D numpy array_like
              Sky-subtracted frame
    """
    # Selecting Normalized region 
    if region is None:
        sample = obj 
    else: 
        ((y1, x1), (y2, x2)) = region 
        sample = obj[ y1:y2, x1:x2 ]

    # Calculating Normalization Factor 
    factor = np.median(sample)

    # De-normalize Sky Frame
    denorm_sky = sky * factor

    # Subtract denorm_sky from object frame
    sky_subtracted = obj - denorm_sky

    return sky_subtracted


# In[4]:


print("Problem 2 continued")

# 3D array to store sky-subtracted frames
no_sky = np.zeros_like(corrected, dtype = float)


# Loop through every dark-subtractd frame
for i in range(corrected.shape[0]):

    # Apply sky subtraction to one 2D frame
    no_sky[i, : , :] = skycormednorm(corrected[i, : , :], 
                                     sky_mednorm)

# Writing last resulting frame to FITS file
last_frame = no_sky[-1, : , :]
fits.writeto("stars_13s_9_nosky.fits", last_frame, overwrite = True)

# Print of requested pixel 
print(f"Value of pixel [217,184] of the last frame is {last_frame[217,184]:.4f}")



# In[ ]:




