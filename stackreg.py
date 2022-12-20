#!/usr/bin/env python3
import pystackreg
import skimage
import numpy as np


# Settings block:

DISTORTION_TYPE = 'RIGID_BODY'
                                # TRANSLATION        - translation
                                # RIGID_BODY         - translation + rotation
                                # SCALED_ROTATION    - translation + rotation + scaling
                                # AFFINE             - translation + rotation + scaling + shearing
                                # BILINEAR           - non-linear transformation; does not preserve straight lines


REFERENCE_FRAME = 'previous'
                                # first, previous, mean


NUMBER_OF_REF_FRAMES = 10
                                # If reference is 'first', then this parameter specifies the
                                # number of frames from the beginning of the stack that
                                # should be averaged to yield the reference image.


MOVING_AVERAGE = 10
                                # If moving_average is greater than 1, a moving average of
                                # the stack is first created (using a subset size of
                                # moving_average) before registration


TIME_AXIS = 0
                                # The axis of the time dimension in original TIFF array (default 0)


DIRECTORY = 'D:/data/files/'
                                # Path to files, leave empty if in the same directory as this script


NOREG = False
                                # Just split stack by channels with no registration, set True or False


QUEUE = [                       # list here TIFF file names without .tif extensions, divided py comma:

    'Your_File_01',
    'Your_File_02',
    'Your_File_03',

]

# End of settings block


def reg(sr, img, ch=None):

    out = sr.register_transform_stack(
        img if ch is None else img[ch],
        reference=REFERENCE_FRAME,
        n_frames=NUMBER_OF_REF_FRAMES,
        moving_average=MOVING_AVERAGE,
        axis=TIME_AXIS,
        verbose=True
    )

    out = out.astype(np.int16)
    return out


def main():

    sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)
    try:
        exec('sr = pystackreg.StackReg(pystackreg.StackReg.{})'.format(DISTORTION_TYPE))
    except:
        print('Missing DISTORTION_TYPE parameter, ')

    for file in QUEUE:

        try:
            img = skimage.io.imread(DIRECTORY + file + '.tif')
        except:

            try:
                img = skimage.io.imread(DIRECTORY + file + '.tiff')
            except:
                print('\nFile', DIRECTORY+file, 'not found')
                continue

        try:

            if img.ndim == 4:

                for ch in range(len(img)):
                    print('\nWorking on file', file, ', channel', ch + 1, '...')
                    
                    if NOREG:
                        out = img[ch]
                    else:
                        out = reg(sr, img, ch)
                            
                    skimage.io.imsave(
                        DIRECTORY + '{}_ch{}{}.tif'.format(
                            file,
                            ch + 1,
                            '_registered' if not NOREG else ''
                        ),
                        out
                    )

            elif img.ndim == 3:
                print('\nWorking on file', file, '...')
                out = reg(sr, img)
                skimage.io.imsave(DIRECTORY + '{}_registered.tif'.format(file), out)
            
            else:
                raise Exception('Wrong TIFF format')

        except:
            print('\n', file, 'Wrong TIFF format, or check TIME_AXIS parameter')
            continue

        print('\nFile', file, 'done!\n')

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
