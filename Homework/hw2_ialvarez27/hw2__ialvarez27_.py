#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Isabella Alvarez
# Homework 2
# September 5, 2026


# In[3]:


# Import commands 
import numpy as np
import matplotlib.pyplot as plt


# In[28]:


# 2a1) Create an array of integers x from 0 to 1000 (up to and including 1000).
x=np.arange(0,1001)
# 1001 elements are needed to include 1000


# In[29]:


# 2a2) Print the datatype of the array and the array’s minimum and maximum.
print(x.dtype)
print(np.min(x))
print(np.max(x))


# In[30]:


# 2b1) Re-scale x to contain values from 0 to 2π.
x = x * ( 2 * np.pi / 1000 )
# The min value is not needed in this formula to rescale
# since the min is staying at zero


# In[31]:


# 2b2) Print the minimum and maximum values of the new x array.
print(np.min(x))
print(np.max(x))


# In[32]:


# 2c) Make an array y whose values are the sine of the values of x
y = np.sin(x)


# In[33]:


# 2d) Print the value of element 234 of y
print(y[234])
# The 234th element would be index 233


# In[58]:


# 3a) Plot y vs. x from problem 2c. Make the plot publication-ready 

# Creating the curve
plt.figure( figsize = (7, 5) )
x=np.linspace(0, 2 * np.pi, 200)
y=np.sin(x)
plt.ylim(-1.5, 1.5)

# Line Characteristics 
plt.plot(x,y,color="blue", linestyle="--", linewidth=3,)

# Labels
plt.title("y = sin(x)", fontsize=14)
plt.xlabel("x (radians)",fontsize=12)
plt.ylabel("y",fontsize=12)

# 3b) Save your plot as a PNG using the appropriate Python commands
plt.savefig('hw2_ialvarez27_problem3b_graph1.png', dpi=300)

# Plotting
plt.show()


# In[59]:


# 4a1) Make a “ramp” array r with 101 evenly spaced elements going from -1 to +1
r=np.linspace(-1,1,101)

# 4a2) “Clip”, or mask, the array so that any value greater than 0.5 is set to 0.5 and
# any value less than -0.5 is set to -0.5. 
r_clipped=np.where( r>0.5, 0.5, np.where(r< -0.5, -0.5, r) )


# In[60]:


# 4b1) In the same plot, plot the original and clipped arrays.

# Graph characteristics
plt.figure( figsize = (7, 5) )
    # Line for original 'r' ramp
plt.plot(r, label='Original', color="blue")
    # Line for clipped 'r' ramp
plt.plot(r_clipped, label='Clipped', color="pink")

# Labels
plt.title("Ramp")
plt.xlabel("X")
plt.ylabel("Y")

# 4b2) Use the appropriate python command to save the plot as a PDF
plt.savefig('hw2_ialvarez27_problem4b_graph2.pdf', format='pdf')

#Plotting
plt.legend()
plt.show()


# In[ ]:


# 5) Give the URLs of two web sites outside of UCF that provide free
# astronomical software that is written in Python. Write a paragraph about each package
# in your own words.

'''
Astropy (https://www.astropy.org/):
Astropy uses Python language to create a collection of software tools specifically for astronomers and astrophysicists. The software can
handle space data such as opening and reading FITS filles which are a common formate used by telescopes to store large data and images.
Units are extremely important when collecting data; Astropy helps keep track of precise astronomical time scales and units, such as 
parsecs and light-years. Along with the units, the software includes built-in constants and standard formulas used in complex
physic porblems. Overall, Astropy helps astronomers code data faster with fewer mistakes.

Sunpy (https://sunpy.org/):
Sunpy is a free, open-source library to help process data tailored to the Sun. This software downloads solar data easily by connecting to
major space archives. Sunpy can also read complex scientific file formats, like FITS, where solar telescope's data is stored. To help 
visuals, Sunpy can take in raw data and turn it into a 2D map of the Sun's surface and atmosphere. Since both the Sun and Earth are 
constantly moving, Sunpy handles the complex geometry calculations whe tracking events over time such as a solar flare. Sunpy is a great
astronomical software that is specialized to the Sun to help ensure complex data and calculations are done correctly.
'''

