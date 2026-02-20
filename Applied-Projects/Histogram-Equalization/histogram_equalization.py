#!/usr/bin/env python
# coding: utf-8

# # Histogram Equalization
# Dai'zjon Carney
# Implement histogram equalization and apply to Cheetah.png. Update show_imghist() to take two images and produce a 2x2 grid of those images and their histograms. The first image should be the original image. The second image should be the histogram equalized image.
 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np

import matplotlib.image as img
import matplotlib.pyplot as plt

from skimage import io
from skimage import exposure
from skimage.util import img_as_float32 as img_as_float


# In[2]:


def print_imginfo(I):
    print(type(I))
    print(I.shape, I.dtype)
    print('Data range:', np.min(I), 'to', np.max(I))


# In[3]:


#def show_imghist(I1, I2):
    # All students
def show_imghist(I1, I2):
     # All students
    fig, ax = plt.subplots(2, 2, figsize=(10,10))
    
    ax[0, 0].imshow(I1, cmap='gray', vmin=0.0, vmax=1.0)
    ax[0, 0].set_axis_off()
    ax[0, 0].set_title('Original Cheetah Image')
    
    ax[1, 0].hist(I1.ravel(), lw=0, bins=256);
    ax[1, 0].set_xlim(0.0,1.0)
    ax[1, 0].set_yticks([])
    
    ax[0, 1].imshow(I2, cmap='gray', vmin=0.0, vmax=1.0)
    ax[0, 1].set_axis_off()
    ax[0, 1].set_title('Histogram Equalized Cheetah Image')
    
    ax[1, 1].hist(I2.ravel(), lw=0, bins=256);
    ax[1, 1].set_xlim(0.0,1.0)
    ax[1, 1].set_yticks([])


# In[4]:


def equalize_hist(I1,nbins=256,use_sqrt=False):
     # ECE 572 students
    I2 = I1
    return I2.astype(I1.dtype, copy=False)


# In[5]:


I1 = io.imread("../cheetah.png", as_gray=True)
I1 = img_as_float(I1)
I2 = exposure.equalize_hist(I1, nbins=256)
print_imginfo(I1)
print_imginfo(I2)
show_imghist(I1, I2)


# In[ ]:




