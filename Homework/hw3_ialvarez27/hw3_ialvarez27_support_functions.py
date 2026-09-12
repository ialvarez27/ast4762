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

   >>> square(5.7)
   32.49

   >>> square(np.array([[2,3],[4,5]]))
   array([[ 4,  9],
          [16, 25]])
"""
    return N ** 2


def squareplot(low, high, space, saveplot=False):
    """ Plots the square of an array over spaced points of a specified range.
    Parameters:
   -----------
   low: takes in `int``or ``float``
         represents the low end of the range
   high: takes in `int``or ``float``
         represent the high end of the range (inclusive)
   space: takes in `int``
          represents number of points to plot
   saveplot: takes in ``str``, gives an optional filename
          to save the plot as a PDF. Defaults to False.
    Returns:
    --------
    matplotlib.figure: Graph of squared array
    
    Examples
    --------
    >>> squareplot(-5 ,5, 100, saveplot="my_sp_pdf")
    Output a graph of x: (-5,5), max y: 25
"""

    # Creates an array x with evenly spaced points
    x = np.linspace(low,high,space)

    # Call the function square to obtain array y
    y = square (x)

    # Plotting
    plt.figure()
    plt.xlabel("Input")
    plt.ylabel("Output")
    plt.title("Square Function")
    plt.plot(x,y)

    # Optional Save Plot
    if saveplot is not False:
        plt.savefig(saveplot, format="pdf")
    plt.show()
    
    

