#!/usr/bin/env python3


################################# Settings block:

DISTORTION_TYPE = 'AFFINE'
                                # TRANSLATION        - translation
                                # RIGID_BODY         - translation + rotation
                                # SCALED_ROTATION    - translation + rotation + scaling
                                # AFFINE             - translation + rotation + scaling + shearing
                                # BILINEAR           - non-linear transformation

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

NOREG = False
                                # Just simple split stack by channels with no registration. Set True or False

MULTIPROCESSING = False
                                # Use all available CPU cores. (Faster, but need much more RAM and can be unstable)

DIRECTORY = 'D:/project/data/'
                                # Path to files, quoted. Leave empty if files in the same directory as this script

TODO_LIST = [                   # list here TIFF file names without .tif extensions, divided py comma:

    'Your_File_01',
    'Your_File_02',
    'Your_File_03',
    'Your_File_04',

]

################################# End of settings block


import numpy as np
import pystackreg
import skimage
import os

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
            skimage.io.imsave(
                DIRECTORY + '{}_registered.tif'.format(
                    file), out)

        else:
            raise Exception('Wrong TIFF format')

    except:
        print('\n', file, 'Wrong TIFF format, or check TIME_AXIS parameter')
        return

    print('\nFile', file, 'done!\n')

    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def main():

    sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)
    try:
        exec('sr = pystackreg.StackReg(pystackreg.StackReg.{})'.format(DISTORTION_TYPE))
    except:
        print('Missing DISTORTION_TYPE parameter, ')

    if MULTIPROCESSING:
        import multiprocessing as mp

        cores = mp.cpu_count()
        pool = mp.Pool(processes=cores)

        print('Found {0} cpu cores, pool of {0} processes created.\n'.format(cores))

        results = [pool.apply_async(process, args=(file, sr,)) for file in TODO_LIST]
        output = [p.get() for p in results]

        print(output)

    else:

        for file in TODO_LIST:
            process(file, sr)

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
