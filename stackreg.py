#!/usr/bin/env python3
import pystackreg
import skimage
import numpy as np


# Settings block:

DISTORTION_TYPE = 'TRANSLATION'    # TRANSLATION, RIGID_BODY, SCALED_ROTATION, AFFINE, BILINEAR
                                   # TRANSLATION        - simple translation
                                   # RIGID_BODY         - translation + rotation
                                   # SCALED_ROTATION    - translation + rotation + scaling
                                   # AFFINE             - translation + rotation + scaling + shearing
                                   # BILINEAR           - non-linear transformation; does not preserve straight lines


REFERENCE_FRAME = 'first'          # first, previous, mean

NUMBER_OF_REF_FRAMES = 10          # If reference is 'first', then this parameter specifies the
                                   # number of frames from the beginning of the stack that
                                   # should be averaged to yield the reference image.

MOVING_AVERAGE = 1                 # If moving_average is greater than 1, a moving average of
                                   # the stack is first created (using a subset size of
                                   # moving_average) before registration

TIME_AXIS = 0                      # The axis of the time dimension in original TIFF array (default 0)

QUEUE = [                          # list here TIFF file names without extensions, divided py comma:

    'A_0010',
    'A_0011',
    'A_0012',
    'A_0013',

]

# End of settings block

def main():

    sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)
    try:
        exec('sr = pystackreg.StackReg(pystackreg.StackReg.{})'.format(DISTORTION_TYPE))
    except:
        print('Missing DISTORTION_TYPE parameter, ')

    for file in QUEUE:

        try:
            img = skimage.io.imread(file + '.tif')
        except:

            try:
                img = skimage.io.imread(file + '.tiff')
            except:
                print('\nFile', file, 'not found')
                continue

        for ch in range(len(img)):

            out = sr.register_transform_stack(
                img[ch],
                reference=REFERENCE_FRAME,
                n_frames=NUMBER_OF_REF_FRAMES,
                moving_average=MOVING_AVERAGE,
                axis=TIME_AXIS,
                verbose=True
                )

            out = out.astype(np.int16)
            skimage.io.imsave('{}_ch{}.tif'.format(file, ch + 1), out)

        print('\n', file, 'done!\n\n')

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
