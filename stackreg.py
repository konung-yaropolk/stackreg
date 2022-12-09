#!/usr/bin/env python3
from pystackreg import StackReg
from skimage import io
import numpy as np



img = io.imread('A_0010.tif') # 3 dimensions : frames x width x height
sr = StackReg(StackReg.TRANSLATION)  # TRANSLATION, RIGID_BODY, SCALED_ROTATION, AFFINE, BILINEAR



ch1=np.array(img[0])
ch2=np.array(img[1])



# register to mean of first 10 images
out_ch1 = sr.register_transform_stack(ch1, reference='first', n_frames=10, verbose=True)
out_ch2 = sr.register_transform_stack(ch2, reference='first', n_frames=10, verbose=True)

out_ch1 = out_ch1.astype(np.int16)
out_ch2 = out_ch2.astype(np.int16)

io.imsave('A_0010_ch1.tif', out_ch1)
io.imsave('A_0010_ch2.tif', out_ch2)








# register each frame to the previous (already registered) one
# this is what the original StackReg ImageJ plugin uses
# out_previous = sr.register_transform_stack(img, reference='previous')

# register to first image
# out_first = sr.register_transform_stack(img, reference='first')

# register to mean image
# out_mean = sr.register_transform_stack(img, reference='mean')


# calculate a moving average of 10 images, then register the moving average to the mean of
# the first 10 images and transform the original image (not the moving average)
# out_moving10 = sr.register_transform_stack(img, reference='first', n_frames=10, moving_average = 10)


