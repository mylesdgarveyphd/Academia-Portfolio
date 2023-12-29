#!/usr/bin/env python
# coding: utf-8

# Intoduction to Functions

# In[1]:


print("This is using the print function")


# Using Functions from Modules

# In[2]:


sqrt(16)


# In[4]:


from math import sqrt


# In[5]:


sqrt(16)


# In[18]:


help("math")


# Import entire module

# In[8]:


import math


# In[10]:


pi


# In[12]:


math.pi


# In[14]:


math.tan(math.pi)


# Using functions in equations.  For example, find $5^6$

# In[16]:


math.pow(5,6)


# In[19]:


5*5*5*5*5*5


# In[21]:


sq16 = math.sqrt(16)


# In[23]:


sq16


# $\frac{1}{\sqrt{2 \sigma \pi}}e^{\frac{(x-\mu)^2}{2\sigma}}$

# In[28]:


sigma=0.1
pi=math.pi
x=3.0
mu=4.0

f=(1/math.sqrt(2*sigma*pi))*math.exp(math.pow((x-mu),2)/(2*sigma))
print(f)


# In[ ]:




