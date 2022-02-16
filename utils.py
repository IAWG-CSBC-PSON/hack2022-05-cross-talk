
"""

Author: 
    Huan Wang (whuan@broadinstitute.org)

Functions:
    imshow()
    intensity_change_at_cell_level()
    plot_co_expression()
    side_by_side()
    run_mesmer()

"""
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import seaborn as sns
import skimage
from skimage.transform import resize, rescale

from deepcell.applications import Mesmer
from deepcell.utils.plot_utils import create_rgb_image
from deepcell.utils.plot_utils import make_outline_overlay


def imshow(src, resize=True, vlim=True, figwidth=10,cmap='viridis'): # cmap='viridis', 'nipy_spectral'
    img = src.copy()
    print ("shape:" ,img.shape)
    figheight = figwidth * img.shape[0]/img.shape[1] 
    if resize:
        img = rescale(img, 0.1, anti_aliasing=False)
        print ("resized shape:" ,img.shape)
    plt.figure(figsize=(figwidth,figheight))
    if vlim:
        plt.imshow(img, vmin= np.quantile(img, 0.01), vmax=np.quantile(img, 0.99), cmap=cmap)
    else:
        plt.imshow(img, cmap=cmap)
    plt.show()


def intensity_change_at_cell_level(df_before, df_after, seg_mask, marker):

    seg_1 = seg_mask.copy()
    seg_2 = seg_mask.copy()
    for i in sorted(np.unique(seg_mask)):
        if i ==0:
            continue
        seg_1 = np.where(seg_1 == i, df_before[marker][i-1], seg_1)
        seg_2 = np.where(seg_2 == i, df_after[marker][i-1], seg_2)
    return seg_1, seg_2


def plot_co_expression(df, x, y, levels=5):

    # Show the joint distribution using kernel density estimation
    sns.set_style("white")
    g = sns.jointplot(data=df, x=x, y=y, linewidth=0.01, alpha=0.7, s=20)
    g.ax_joint.set(xlim=(0, np.percentile(df[x],99.5)))
    g.ax_joint.set(ylim=(0, np.percentile(df[y],99.5)))
    g.plot_joint(sns.kdeplot, color="r", zorder=1, levels=levels)
    plt.tight_layout()
    plt.show()

    
def side_by_side(arr1, arr2, figsize, title1="", title2="", resize=True, same_vlim=False, cmap='viridis'):  # cmap='viridis', cmap='nipy_spectral'
    
    if resize:
        arr1 = rescale(arr1, 0.1, anti_aliasing=False)
        print ("resized shape:" ,arr1.shape)
        arr2 = rescale(arr2, 0.1, anti_aliasing=False)
        print ("resized shape:" ,arr2.shape)        
        
    fig, ax = plt.subplots(1, 2, figsize=figsize)
    
    ax[0].imshow(arr1, vmin=np.min(arr1), vmax=np.max(arr1), cmap=cmap)
    if same_vlim:
        ax[0].imshow(arr1, vmin=np.min(arr2), vmax=np.max(arr2), cmap=cmap)
    ax[1].imshow(arr2, vmin=np.min(arr2), vmax=np.max(arr2), cmap=cmap)
    
    ax[0].set_title(title1)
    ax[1].set_title(title2)
    plt.show() 
    

def run_mesmer(im1, im2, image_mpp=0.5, compartment='whole-cell'):
    
    print ('start mesmer process...')
    # Convert to 4D array
    im = np.stack((im1, im2), axis=-1)
    im = np.expand_dims(im,0)

    # create rgb overlay of image data for visualization
    rgb_images = create_rgb_image(im, channel_colors=['green', 'blue']) 
        
    # Create the application
    app = Mesmer()

    # create the label
    labeled_image = app.predict(im, image_mpp=image_mpp, compartment=compartment)
    mask = labeled_image[0,...,0]
    print ('generating mask...')

    # Create the mask
    boundary = make_outline_overlay(rgb_data=rgb_images, predictions=labeled_image)[0,...,0] 
    print ('mask is generated.')
    return mask, boundary


