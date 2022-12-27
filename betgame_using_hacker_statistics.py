#!/usr/bin/env python
# coding: utf-8

# ## Use hacker statistics to calculate your chances of winning a bet: what's the estimated chance that you'll reach at least 60 steps high if you play this Empire State Building game?

# In[4]:


import numpy as np


# #### Set the seed

# In[5]:


np.random.seed(123)


# Generate random float and stimulate the dice

# In[6]:


print(np.random.rand())
print(np.random.randint(1,7))
print(np.random.randint(1,7))


# #### intinal 

# In[7]:

# Gernerate a list of random walk
random_walk=[0]
for x in range(100):
    step = random_walk[-1]
    dice = np.random.randint(1,7)
    if dice <=2: 
        step = max(0, step + 1)
# use max to make sure step can't go below 0
    elif dice <= 5: 
        step = step - 1
    else: 
        step = step + np.random.randint(1,7)
    random_walk.append(step)
print(random_walk)


# #### plot 

# In[2]:


import matplotlib.pyplot as plt


# In[8]:


plt.plot(random_walk)
plt.show()


# #### stimulate 500 times 

# In[10]:


all_walks = []
for i in range(500):
    random_walk=[0]
    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <=2: 
# use max to make sure step can't go below 0
            step = max(0, step - 1)
        elif dice <= 5: 
            step = step + 1
        else: 
            step = step + np.random.randint(1,7)
            
        if np.random.rand() < 0.001:
            step = 0
# 0.1% chance of falling down
        random_walk.append(step)
    all_walks.append(random_walk)


# In[11]:


plt.plot(all_walks)
plt.show()


# In[12]:


tras_walk = np.transpose(np.array(all_walks))
print(tras_walk)
plt.plot(tras_walk)
plt.show()


# In[13]:


## Select last row 
ends = tras_walk[-1,:]
plt.hist(ends)
plt.show()


# ### what's the estimated chance that you'll reach at least 60 steps high if you play this Empire State Building game? 78.4%
