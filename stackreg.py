#!/usr/bin/env python3
import multiprocessing
import numpy as np
import pystackreg
import skimage
import os

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


DIRECTORY = 'data/'
                                # Path to files, leave empty if in the same directory as this script


NOREG = True
                                # Just split stack by channels with no registration, set True or False


TODO_LIST = [                   # list here TIFF file names without .tif extensions, divided py comma:

    'A_0008',
    'A_0009',
    'A_0010',
    'A_0011',

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

def process(file, sr):

    try:
        img = skimage.io.imread(DIRECTORY + file + '.tif')
    except:

        try:
            img = skimage.io.imread(DIRECTORY + file + '.tiff')
        except:
            print('\nFile', DIRECTORY + file, 'not found')
            return

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
        return

    print('\nFile', file, 'done!\n')

    #print('parent process:', os.getppid())
    #print('process id:', os.getpid())


def main():

    sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)
    try:
        exec('sr = pystackreg.StackReg(pystackreg.StackReg.{})'.format(DISTORTION_TYPE))
    except:
        print('Missing DISTORTION_TYPE parameter, ')

    cores = multiprocessing.cpu_count()
    print('Found {0} cores, running in {0} processes.\n'.format(cores))

    for file in TODO_LIST:
       # process(file, sr)
        p = multiprocessing.Process(target=process, args=(file, sr,))
        p.start()
        p.join()
        print('parent process:', os.getppid())
        print('process id:', os.getpid())

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
