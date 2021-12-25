%matplotlib inline
import matplotlib.pyplot as plt
from skimage import color
import numpy as np
import imageio

def show_fft_image(im):
    f, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(20,30))
    ax1.imshow(im)
    ax1.axis('equal')
    ax1.axis('off')
    ax1.set_title('Original Image')
    gray = color.rgb2gray(im);
    ax2.imshow(gray, cmap='gray')
    ax2.axis('equal')
    ax2.axis('off')
    ax2.set_title('gray image')
    Fs = np.fft.fft2(gray)
    F2 = np.fft.fftshift( Fs ) 
    psd2D = np.abs( F2 )#**2
    ax3.imshow( np.log10(psd2D))
    ax3.axis('equal')
    ax3.axis('off')
    ax3.set_title('frequency space')
    
filename = './images/fft/brick_texture3420.jpg'
im = imageio.imread(filename)
show_fft_image(im)

filename = './images/img009000A.jpg'
im = imageio.imread(filename)
show_fft_image(im)


import os

directory = './images/fft/'
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        print(os.path.join(directory, filename))
    else:
        continue
        
        
filename = './images/fft/pexels-photo.jpg'
im = imageio.imread(filename)
show_fft_image(im)

filename ='./images/fft/codes_splash.jpg'
im = imageio.imread(filename)
show_fft_image(im)


filename = './images/fft/152203-004-A1BA21F3.jpg'
im = imageio.imread(filename)
show_fft_image(im)

filename = './images/fft/brick-wall-angle-23441280781042zHov.jpg'
im = imageio.imread(filename)
show_fft_image(im)


