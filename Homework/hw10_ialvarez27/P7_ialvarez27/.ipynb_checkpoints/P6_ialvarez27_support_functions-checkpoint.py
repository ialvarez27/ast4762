
# Imports
import numpy as np



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
