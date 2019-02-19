#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
get_ipython().run_line_magic('matplotlib', 'inline')


# In[9]:


get_ipython().system(' curl -O https://i5.walmartimages.ca/images/Large/428/5_r/6000195494285_R.jpg')


# In[28]:


img=plt.imread('6000195494285_R.jpg')
plt.imshow(img)


# In[31]:


filename="6000195494285_R.jpg"
image=Image.open(filename)
size=width ,height=image.size;
coordinate=x,y=180,69
print image.getpixel(coordinate)


# In[ ]:




