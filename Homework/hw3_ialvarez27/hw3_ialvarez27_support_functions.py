"""
Explain the purpose of this file

"""

# Import Libraries

import os
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import astropy.io.fits as fits


def square(N):
    """Calculates the squre of a scalar or array of any dimension.

   Parameters:
   -----------
   N: ``int``, ``float``, or ``array_like``.

   Returns:
   --------
   ``int``, ``float``, or ``array_like``
    The square of the input element(s)

   Examples
   --------
   >>> square (5)
   25

   >>> square(np.array([2,4,6]))
   array([ 4, 16, 36])
"""
    return N ** 2

