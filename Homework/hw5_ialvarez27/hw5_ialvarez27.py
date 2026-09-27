#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Isabella Alvarez
# Homework 5
# September 25, 2026


# In[1]:


import numpy as np              # load numerical module
import matplotlib.pyplot as plt # load plotting module
from hw5_ialvarez27_support_functions import sigrej #Function made for Problem 3


# In[2]:


# Needed code from Practicum 3

# Poission Distribution 
good = np.random.poisson(10000, 396) # Draws 396 random photon counts

# Uniform Distribution 
bad = np.random.uniform(0, 1e6, 4) # Draws 4 random numbers between 0 and 10^6

# Combine Both Arrays
sample = np.concatenate((good, bad))

# Subsample
std = np.std(sample)
median = 10010.0
subsample = sample[ np.abs(sample - median) < 5 * std ]

# Subsample Statistics
print(f"Mean: {np.mean(subsample)}")
print(f"Median: {np.median(subsample)}")
print(f"Standard Deviation: {np.std(subsample)}")


# In[3]:


print("Question 2:")

# Recalculating Statistics
new_std = np.std(subsample)
new_median = np.median(subsample)

# Creating sub-subsample 
sub_sample_2 = subsample [ np.abs(subsample - new_median) < 5 * new_std ] 
print(f"Mean: {np.mean(sub_sample_2)}")
print(f"Median: {np.median(sub_sample_2)}")
print(f"Standard Deviation: {np.std(sub_sample_2)}")

# Answering questions 
print("\n1.How different are the final mean and median?")
print("The final mean about 248 lower than the first subsample.")
print("-> This indicates the second round of sigma clipping eliminated extreme outliers.")
print("The final median is only lowered by 1, which is expected since it is less affected by outliers.")
print("\n2.How close is the final standard deviation to that expected for the Poisson distribution?")
print("The final std, 104.29, is very close to the expected std of 100. Sigma clipping was successful.")
print("\n3.Will this method always remove every bad pixel?")
print("No, this method has a limition of the boundary 5-sigma.")


# In[5]:


print ("Question 3:")
# Running sigrej() on data from Question 2
clean_mask = sigrej(sample, (5,5))

# Applying mask for good data
clean_data = sample [clean_mask]

print(f"Mean of cleaned data: {np.mean(clean_data)}")


# In[ ]:




