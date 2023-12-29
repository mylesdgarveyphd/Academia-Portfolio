#!/usr/bin/env python
# coding: utf-8

# Let's look a quick example problem.  Suppose we wanted to generate a random even number from 1 to a given number $n$.

# In[5]:


import random

n=10
k=5
even_numbers = range(0,2*n,2)
even_numbers

random.sample(even_numbers,k)


# Suppose we want to generalize this so that all we need to do is run a single function with inputs $n$ and $k$.  How do we do this?  We define our own function!

# In[6]:


def generate_even_numbers(n,k):
    even_numbers=range(0,2*n,2)
    return random.sample(even_numbers,k)


# Now let's use our own function!

# In[8]:


generate_even_numbers(100,20)


# In[12]:


generate_even_numbers(10,2)


# Likewise, we can define a function to give us random odd numbers:

# In[14]:


def generate_odd_numbers(n,k):
    odd_numbers=range(1,2*n+1,2)
    return random.sample(odd_numbers,k)


# In[16]:


generate_odd_numbers(10,4)


# In[21]:


generate_odd_numbers(20,6)


# In[ ]:




