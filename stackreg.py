#!/usr/bin/env python3

import numpy as np
import pystackreg
import tiffile
import settings as s



sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)

def transform(img, transform_matrix):

    out = sr.transform_stack(
        img,
        tmats=transform_matrix)
    out = out.astype(np.int16)
    return out


def register(img, 
            REFERENCE_FRAME,
            NUMBER_OF_REF_FRAMES,
            MOVING_AVERAGE,
            TIME_AXIS,
            verbose=False):

    transform_matrix = sr.register_stack(
        img,
        reference=REFERENCE_FRAME,
        n_frames=NUMBER_OF_REF_FRAMES,
        moving_average=MOVING_AVERAGE,
        axis=TIME_AXIS,
        verbose=verbose)

    return transform_matrix


def process(
        file, 
        DIRECTORY=s.DIRECTORY,
        DISTORTION_TYPE=s.DISTORTION_TYPE,
        REFERENCE_FRAME=s.REFERENCE_FRAME,
        NUMBER_OF_REF_FRAMES=s.NUMBER_OF_REF_FRAMES,
        MOVING_AVERAGE=s.MOVING_AVERAGE,
        TIME_AXIS=s.TIME_AXIS,
        SPLIT_ONLY=s.SPLIT_ONLY,
        verbose=False):

    try:
        exec('sr = pystackreg.StackReg(pystackreg.StackReg.{})'.format(DISTORTION_TYPE))
    except:
        print('Missing DISTORTION_TYPE parameter, used default "TRANSLATION"')
    print(file)
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

            transform_matrix_list = np.empty((1, len(img[0]), 3, 0))
            transform_matrix = np.array([])

            if not SPLIT_ONLY:

                for ch in range(len(img)):
                    print('\nRegistrating file', file, ', channel', ch + 1, '...')

                    transform_matrix_list = np.append(
                        transform_matrix_list,
                        [register(
                            img[ch],
                            REFERENCE_FRAME,
                            NUMBER_OF_REF_FRAMES,
                            MOVING_AVERAGE,
                            TIME_AXIS,
                            verbose=verbose)],
                        axis=-1)

                transform_matrix = np.mean(
                    transform_matrix_list,
                    axis=0)

            for ch in range(len(img)):

                if not SPLIT_ONLY:

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
                        '_registered' if not SPLIT_ONLY else ''),
                    out)


        elif img.ndim == 3 and not SPLIT_ONLY:

            print('\nWorking on file', file, '...')

            out = transform(
                        img,
                        register(
                            img,
                            REFERENCE_FRAME,
                            NUMBER_OF_REF_FRAMES,
                            MOVING_AVERAGE,
                            TIME_AXIS,
                            verbose=False)
                        )

            print('\nWriting to file...')

            tiffile.imwrite(
                '{}{}_registered.tif'.format(
                    DIRECTORY,
                    file),
                out)

        elif img.ndim == 3 and SPLIT_ONLY == True:
            raise Exception('SPLIT_ONLY option is activated, there is nothing to do with single-channel image file')

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

    if s.MULTIPROCESSING:
        import multiprocessing as mp

        cores = mp.cpu_count()
        pool = mp.Pool(processes=cores)

        print('\n{0} cpu cores found, pool of {0} processes created.\n'.format(cores))

        results = [pool.apply_async(process, args=(line,)) for line in s.TODO_LIST]
        output = [p.get() for p in results]

        print('Errors:',output)

    else:

        for line in s.TODO_LIST:
            print(line)
            process(line, verbose=True)

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
