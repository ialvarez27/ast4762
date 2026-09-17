#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Isabella Alvarez
# HW 4
# September 16, 2026


# In[15]:


import numpy as np
import matplotlib.pyplot as plt


# In[16]:


print("Problem 2(a):")

N = 10000    # 10,000 draws

# Population Parameters
mu, sigma = 55, 13

# Random Generation code
sample = np.random.normal( mu, sigma, N )

print ( f" Generated {N} random draws from Gaussian distribution" )
print ( f" Parameters: Mean (mu) = {mu}, Standard Deviation (sigma) = {sigma}" )


# In[27]:


print("Problem 2(b):")

bins = np.arange( 0, 101, 1 )  # bins from x=0 to 100 with a width of 1 unit

# Plotting
plt.figure(figsize = (10, 6))
plt.hist(sample, bins, color = "skyblue", edgecolor = "black")
plt.xlabel("x")
plt.ylabel("N (x)")
plt.title("Histogram of a Gaussian")

# Saving graph 
plt.savefig('hw4_ialvarez27_problem2b_graph1.png', dpi = 300)

plt.show()


# In[28]:


print("Problem 2(c):")

bin_center = np.arange(0.5, 100., 1) # evaluating at the center of each bin

# The Gaussian
gaussian = ( 1/ (sigma * np.sqrt (2 * np.pi))) * np.exp(-(bin_center-mu)**2 / (2 * (sigma**2)))

# Converting the probability into expected counts
expected = N * gaussian 

# Plotting the histogram
plt.figure(figsize = (10, 6))
plt.hist(sample, bins)

# Overplotting the histogram
plt.plot( x, expected, linewidth = 2, color = "red")
plt.xlabel("x")
plt.ylabel("N(x)")
plt.title("Histogram of a Gaussian")

# Saving graph
plt.savefig('hw4_ialvarez27_problem2c_graph1.png', dpi = 300)

plt.show


# In[ ]:




