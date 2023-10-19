#!/usr/bin/env python3

import numpy as np
import pystackreg
import tifffile
import settings as s



def transform(
        img, 
        sr, 
        transform_matrix):

    out = sr.transform_stack(img, tmats=transform_matrix)
    out = out.astype(np.int16)

    return out


def register(
        img, 
        sr,
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
   
    match DISTORTION_TYPE:
        case 'TRANSLATION'          : sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)
        case 'RIGID_BODY'           : sr = pystackreg.StackReg(pystackreg.StackReg.RIGID_BODY)
        case 'SCALED_ROTATION'      : sr = pystackreg.StackReg(pystackreg.StackReg.SCALED_ROTATION)
        case 'AFFINE'               : sr = pystackreg.StackReg(pystackreg.StackReg.AFFINE)
        case 'BILINEAR'             : sr = pystackreg.StackReg(pystackreg.StackReg.BILINEAR)
        case _                      : sr = pystackreg.StackReg(pystackreg.StackReg.TRANSLATION)

    # Bad construction, to review:
    try:
        img = tifffile.imread(DIRECTORY + file + '.tif')
    except:

        try:
            img = tifffile.imread(DIRECTORY + file + '.tiff')
        except Exception as e:
            print('\n!!! File:', DIRECTORY + file, 'not found')
            return e

    try:

        print('\n>>> Started working with the file', file, '...')
        # algorytm for 4-dimentional tiff:        
        if img.ndim == 4:

            transform_matrix_list = np.empty((1, len(img[0]), 4, 0))
            transform_matrix = np.array([])

            if not SPLIT_ONLY:    # Bad construction with SPLIT_ONLY, to review

                for ch in range(len(img)):
                    if verbose: print('\nRegistrating file', file, ', channel', ch + 1, '...')

                    transform_matrix_list = np.append(
                        transform_matrix_list,
                        [register(
                            img[ch],
                            sr,
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

                if not SPLIT_ONLY:    # Bad construction with SPLIT_ONLY, to review

                    if verbose: print('\nTransforming file', file, ', channel', ch + 1, '...')
                    out = transform(
                        img[ch],
                        sr,
                        transform_matrix)

                else:
                    out = img[ch]

                tifffile.imwrite(
                    '{}{}_ch{}{}.tif'.format(
                        DIRECTORY,
                        file,
                        ch + 1,
                        '_registered' if not SPLIT_ONLY else ''),
                    out)

        # algorytm for 3-dimentional tiff:
        elif img.ndim == 3 and not SPLIT_ONLY:    # Bad construction with SPLIT_ONLY, to review
        
            out = transform(
                        img,
                        sr,
                        register(
                            img,
                            sr,
                            REFERENCE_FRAME,
                            NUMBER_OF_REF_FRAMES,
                            MOVING_AVERAGE,
                            TIME_AXIS,                            
                            verbose=False)
                        )

            if verbose: print('\nWriting to file...')

            tifffile.imwrite(
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
        return e

    else:
        print('\n*** File', file, 'done!')
        
    # immediatly clearing memory used by np arrays
    finally:
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

        cores = mp.cpu_count()          # CPU cores count
        files = len(s.TODO_LIST)        # Files to do count
        processes = min(cores, files)
        pool = mp.Pool(processes)

        print('\nParallel processing mode activated:\n{0} cpu cores per queue of {1} files found, pool of {2} processes created.\nPlease, ensure if you have enough RAM for multiprocessing\n'.format(cores, files, processes))

        results = [pool.apply_async(process, args=(line[0],) if isinstance(line, list) else (line,), kwds=line[1] if isinstance(line, list) else {}) for line in s.TODO_LIST]
        output = [p.get() for p in results]

        print('\nErrors:',output)

    else:
        
        for line in s.TODO_LIST:

            if isinstance(line, list):                
                process(line[0], **line[1], verbose=True)
            else:
                process(line, verbose=True)

    print('\nSeries done!\n')


if __name__ == '__main__':
    main()
