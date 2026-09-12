#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Isabella Alvarez
# HW 3
# September 12, 2026


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
import importlib
from hw3_ialvarez27_support_functions import square
from hw3_ialvarez27_support_functions import squareplot 


# In[6]:


print("Problem 2 (h):")

# Creates an array from 0-9
test_square_1 = np.arange(10)

print(square(test_square_1))


# In[7]:


print("Problem 2 (i):")

# Prints an array of 25 that contains floats 5x5 
test_square_2 = np.arange(25, dtype=float).reshape(5,5)

print(square(test_square_2))


# In[8]:


print("Problem 3: ")

# low = 1, high = 7, num_points = 5
squareplot(1, 7, 5, saveplot="hw3_ialvarez27_Problem3_graph.pdf")


# In[ ]:




