#!/usr/bin/env python
# coding: utf-8

# 
# What is a list?  A list is a collection of objects indexed in a way that starts at 0 and ends at the $n-1$

# In[2]:


#Different variables for each number.
x1=5
x2=6
x3=2
x4=5
x5=7

(x1+x2+x3+x4+x5)/5


# In[4]:


x=[5,6,2,5,7]


# In[6]:


x


# In[8]:


x[2]


# In[11]:


len(x)


# In[14]:


sum(x)


# In[16]:


sum(x)/len(x)


# In[18]:


x[2]=10


# In[19]:


x


# In[21]:


x=[x,5]


# In[22]:


x


# In[24]:


len(x)


# In[25]:


x[0]


# In[26]:


len(x[0])


# In[27]:


x=x[0][0]


# In[28]:


x


# In[39]:


x+=[30]


# In[47]:


x


# In[36]:


y=x


# In[41]:


y


# In[43]:


from operator import itemgetter


# In[45]:


itemgetter(0,2,len(x)-1)(x)


# In[48]:


45 in x


# In[49]:


45 not in x


# In[50]:


30 in x


# In[ ]:




