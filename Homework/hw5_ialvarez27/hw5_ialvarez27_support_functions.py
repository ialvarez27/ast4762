
"""
This support function will be used to reject bad data points.

"""


# Import Libraries
import numpy as np



def sigrej(data, limits, mask = None):
    """ Iterative sigma rejection on an array of data.

        Parameters:
        -----------
        data: numerical array_like 
              an array containing data points.
        limits: tuple of float or int
                represents the sigma rejection limits. 
                for each iteration.
        mask: numerical array_like, optional
              Boolean array with the same shape as data.
              True indicates good data points and False i
              ndicates bad data points. If None, all data are
              initially considered good.
        
        Returns:
        --------
        mask: numerical array_like of bool.
              modified Boolean mask where rejected
              data points are False.

        Example
        -------
        >>> import numpy as np
        >>> data = np.array([10.0, 10.4, 100, 9.8])
        >>> sigrej(data, (1.0,))
        array([ True,  True, False,  True])
    """
    # If no mask is given, initially all data is good
    if mask is None:
        mask = np.ones_like(data, dtype = bool)

    # Iterate through each rejection limit from tuple
    for N in limits:

        # use only the data considered good
        good_data = data[mask]
        
        # Stop if no good data points remain
        if len(good_data) == 0:
            break

        # Calculate statistics of good data 
        mean = np.mean(good_data)
        std  = np.std(good_data)

        # Keep points within N std
        mask = mask & (np.abs(data-mean) < N * std)
    
    # Return final Boolean mask
    return mask
