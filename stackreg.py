#!/usr/bin/env python3
################################# Settings block:

TODO_LIST = [                   # list here quoted TIFF file names without .tiff extensions, separated by comma:

    # 'Your_File_01',
    # 'Your_File_02',
    # 'Your_File_03',

]

DIRECTORY = 'data/'
                                # Path to files. Leave quotes empty if the files in the same directory with this script

DISTORTION_TYPE = 'BILINEAR'
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
                                # Use all available CPU cores.
                                # Faster, but need much more RAM so can be unstable.

################################# End of settings block



import numpy as np
import pystackreg
import tiffile


sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)

def transform(img, transform_matrix):

    out = sr.transform_stack(
        img,
        tmats=transform_matrix)
    out = out.astype(np.int16)
    return out


def register(img, verbose=False):

    transform_matrix = sr.register_stack(
        img,
        reference=REFERENCE_FRAME,
        n_frames=NUMBER_OF_REF_FRAMES,
        moving_average=MOVING_AVERAGE,
        axis=TIME_AXIS,
        verbose=verbose)

    return transform_matrix


def process(file, **kwarg):

    try:
        img = tiffile.imread(DIRECTORY + file + '.tif')
    except:

        try:
            img = tiffile.imread(DIRECTORY + file + '.tiff')
        except:
            print('\nFile:', DIRECTORY + file, 'not found')
            return

    try:

        if img.ndim == 4:

            transform_matrix_list = np.empty(1, len(img[0]), 3, 0)
            transform_matrix = np.array([])

            if not NOREG:

                for ch in range(len(img)):
                    print('\nRegistrating file', file, ', channel', ch + 1, '...')

                    transform_matrix_list = np.append(
                        transform_matrix_list,
                        [register(
                            img[ch],
                            **kwarg)],
                        axis=-1)

                transform_matrix = np.mean(
                    transform_matrix_list,
                    axis=0)

            for ch in range(len(img)):

                if not NOREG:

                    print('\nTransforming file', file, ', channel', ch + 1, '...')
                    out = transform(
                        img[ch],
                        transform_matrix)

                else:
                    out = img[ch]


                tiffile.imwrite(
                    '{}{}_ch{}{}.tif'.format(
                        DIRECTORY,
                        file,
                        ch + 1,
                        '_registered' if not NOREG else ''),
                    out)


        elif img.ndim == 3 and not NOREG:

            print('\nWorking on file', file, '...')

            out = transform(
                        img,
                        register(
                            img,
                            **kwarg)
                        )

            tiffile.imwrite(
                '{}{}_registered.tif'.format(
                    DIRECTORY,
                    file),
                out)

        elif img.ndim == 3 and NOREG == True:
            raise Exception('NOREG option is activated, there is nothing to do with the file')

        else:
            raise Exception('Wrong TIFF format, or check TIME_AXIS parameter')

    except Exception as e:
        print('An error occured when processing {}:\n{}'.format(file, e))
        return

    else:
        print('\nFile', file, 'done!\n')

    finally:    # immediatly clearing memory used by np arrays
        img = None
        del img
        transform_matrix_list = None
        del transform_matrix_list
        transform_matrix = None
        del transform_matrix
        out = None
        del out



def main():

    try:
        exec('sr = pystackreg.StackReg(pystackreg.StackReg.{})'.format(DISTORTION_TYPE))
    except:
        print('Missing DISTORTION_TYPE parameter, used default "TRANSLATION"')


    if MULTIPROCESSING:
        import multiprocessing as mp

        cores = mp.cpu_count()
        pool = mp.Pool(processes=cores)

        print('\n{0} cpu cores found, pool of {0} processes created.\n'.format(cores))

        results = [pool.apply_async(process, args=(file,)) for file in TODO_LIST]
        output = [p.get() for p in results]

        print('Errors:',output)

    else:

        for file in TODO_LIST:
            process(file, verbose=True)

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
