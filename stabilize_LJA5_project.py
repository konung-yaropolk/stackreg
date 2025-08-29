#!/usr/bin/env python3

# Global settings block
# Theese parameters are used by default if nothing specified for given movie in the TO_DO_LIST

DIRECTORY = 'data/'
# Provide full path to files. Leave quotes empty if the files in the same directory with this script

DISTORTION_TYPE = 'BILINEAR'
# TRANSLATION        - translation
# RIGID_BODY         - translation + rotation
# SCALED_ROTATION    - translation + rotation + scaling
# AFFINE             - translation + rotation + scaling + shearing
# BILINEAR           - non-linear transformation (no support for 'previous' reference frame mode)

# to indentify it open the original tiff file and see which moving occurred
# (most often it's translation, affine or bilinear)
# In severe distortion cases stabilization can be processed multiple times with different parameters.
# Transformations can be applied subsequently on the same file with different name,
# f.e. first run “transformation” and then “bilinear”


REFERENCE_FRAME = 'first'
# Can be first, previous, or mean, most often first is the best option. In severe distortion
# cases stabilization can be processed multiple times with different parameters.
# f.e. first run "previous" and then "first".

NUMBER_OF_REF_FRAMES = 15
# If reference is 'first', then this parameter specifies the
# number of frames from the beginning of the stack that
# should be averaged to yield the reference image.

MOVING_AVERAGE = 15
# If moving_average is greater than 1, a moving average of
# the stack is first created (using a subset size of
# moving_average) before registration

REFERENCE_CHANNEL = 0
# what channel use as refferense, 0 - use mean of all

TIME_AXIS = 0
# The axis of the time dimension in original TIFF array (default 0)

SPLIT_ONLY = False
# Just simple split stack by channels with no registration. Set True or False

TAKE_ALL_FILES = False
# Process all .tif files recurcively in given directory
# If this parameter turned on, TODO_LIST will be ignored

SAVE_TRANSFORM_MATRIX = True
# Save transform matrix in .npy file with the same filename as original .tif

READ_TRANSFORM_MATRIX = False
# Read transform matrix from .npy file with the same filename as original .tif

MULTIPROCESSING = False
# Use all available CPU cores.
# Faster, but need much more RAM so can be unstable.

PROCESSES_LIMIT = 10
# Maximum size of multiprocessing pull
# Set the maximum of processes if there isn't enough RAM
# Set 0 or None to use as many processes as possible


# list here quoted TIFF file names without .tiff extensions, separated by comma:
TODO_LIST = [


    # ['Field_7_Dynorphin_application_ch2',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/2-photon/PI_Pirt_GCamp3_x_Thy1_RGeco_PP_and_fiber_typing/2025_05_12/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'NUMBER_OF_REF_FRAMES': 20,
    #         'MOVING_AVERAGE': 20,
    #     }
    #  ],


    # ['Field_1_Dynorphin_application',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/Stacey/LJA5 project Dynorphin control/2025_08_22/',
    #         'DISTORTION_TYPE': 'TRANSLATION',
    #         'REFERENCE_FRAME': 'first',
    #         'NUMBER_OF_REF_FRAMES': 20,
    #         'MOVING_AVERAGE': 20,
    #     }
    #  ],

    ['Field_1_Dynorphin_application',
        {
            'DIRECTORY': 'F:/Lab Work Files/Stacey/LJA5 project Dynorphin control/2025_08_25/',
            'DISTORTION_TYPE': 'AFFINE',
            'REFERENCE_FRAME': 'first',
            'NUMBER_OF_REF_FRAMES': 20,
            'MOVING_AVERAGE': 20,
        }
     ],

    # ['Field_1',
    #     {
    #         'DIRECTORY': 'F:/Lab Work Files/Stacey/LJA5 project Dynorphin control/2025_08_26/',
    #         'DISTORTION_TYPE': 'BILINEAR',
    #         'REFERENCE_FRAME': 'first',
    #         'NUMBER_OF_REF_FRAMES': 20,
    #         'MOVING_AVERAGE': 20,
    #     }
    #  ],







]

if __name__ == '__main__':
    import stackreg
    stackreg.main()
