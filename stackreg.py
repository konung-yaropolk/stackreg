#!/usr/bin/env python3
from pystackreg import StackReg
from skimage import io
import numpy as np

QUEUE = [   

# list here tif file names without extensions, divided py comma

'A_0010',    
'A_0011',
'A_0012',
'A_0013',

]


for file in QUEUE:


    img = io.imread(file+'.tif') # 3 dimensions : frames x width x height


    sr = StackReg(StackReg.TRANSLATION)  # TRANSLATION, RIGID_BODY, SCALED_ROTATION, AFFINE, BILINEAR

    for ch in range(len(img)):        

        # register to mean of first 10 images
        out = sr.register_transform_stack(img[ch], reference='first', n_frames=10, verbose=True)
        out = out.astype(np.int16)
        io.imsave('{}_ch{}.tif'.format(file, ch+1), out)

    print('\n',file,'done!\n\n')

print('Series done!\n')



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


