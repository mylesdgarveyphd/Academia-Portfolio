#!/usr/bin/env python
# coding: utf-8

# So there are two forms of "Logic Control": Conditionals and Iterations

# First, we look at "if-else" statements.  The thing to remember here is that after you put "if", you need to put a "condition" (in the example below, the "condition" is x==5).  Then after the condition, you type ":", then enter, then tab, although, in Jupyter Notebook, the tab is automatically put in.  If working in a text file, you absolutely need to ensure that the tab is there.

# In[1]:


x=6


# In[2]:


if x == 5:
    print("X is indeed equal to 5")
else:
    print("X is NOT equal to 5!")


# In[3]:


x==5


# In[4]:


if x%2==0:
    x=x+2
    x=3*x
else:
    x=x+3
    x=2*x


# In[5]:


x


# In[6]:


x=5


# What would happen if we forgot to put the tabs?

# In[7]:


if x%2==0:
    x=x+2
x=3*x


# In[8]:


x


# When we run that code, if $x=5$, then we get $15$ instead of $5$.  If its odd, we didn't want to change the number $x$.  How do to fix this?  Easy!  Add a tab!

# In[9]:


x=5
if x%2==0:
    x=x+2
    x=3*x


# In[10]:


x


# What about iterations?  Well, there are two types of iteration: for loops and while loops.  Let's first look at while loops:

# In[11]:


x=1

x+=1
x+=1
x+=1


# How can run the code above in a shorter way?

# In[12]:


x=1

while x<=4:
    x+=1
    print(x)


# In[13]:


x


# In[14]:


x<=4


# The For Loop:

# In[15]:


theNumbers=range(1,26,1)
print(theNumbers)
#Iterate through the list and check is each number is divisible by 3:
for i in theNumbers:
    if i%3==0:
        print("It's divisible by 3!")
    else:
        print("It's not divisible by 3!")
        
print("We're Done!")


# In[16]:


theNumbers


# In[17]:


#Alternative Execution:
theNumbers=range(1,26,1)
print(theNumbers)
#Iterate through the list and check is each number is divisible by 3:

i=theNumbers[0]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[1]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[2]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[3]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[4]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[5]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[6]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[7]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[8]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[9]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[10]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[11]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[12]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[13]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[14]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[15]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[16]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[17]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[18]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[19]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[20]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[21]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[22]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

i=theNumbers[23]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")
i=theNumbers[24]
if i%3==0:
    print("It's divisible by 3!")
else:
    print("It's not divisible by 3!")

print("We're Done!")
    
    


# Let's make a number guessing game!

# In[19]:


import random

randNumber = random.randint(1,10)
print("Guess a Number!")

guess=int(input())
theCount = 1

while(guess!=randNumber and theCount<5):
    print("You got the guess wrong!  Try again:")
    guess=int(input())
    theCount+=1
    if(guess==randNumber):
        print("You Won the Game!")
        
if(guess!=randNumber):
    print("You Lost the Game!")


# In[ ]:




