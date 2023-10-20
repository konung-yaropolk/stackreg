################################# Settings block:


DIRECTORY = 'data/'
                                # Path to files. Leave quotes empty if the files in the same directory with this script

DISTORTION_TYPE = 'BILINEAR'
                                # TRANSLATION        - translation
                                # RIGID_BODY         - translation + rotation
                                # SCALED_ROTATION    - translation + rotation + scaling
                                # AFFINE             - translation + rotation + scaling + shearing
                                # BILINEAR           - non-linear transformation

REFERENCE_FRAME = 'first'
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

SPLIT_ONLY = False
                                # Just simple split stack by channels with no registration. Set True or False

MULTIPROCESSING = False
                                # Use all available CPU cores.
                                # Faster, but need much more RAM so can be unstable.


TODO_LIST = [                   # list here quoted TIFF file names without .tiff extensions, separated by comma:



# # Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS + PMX205 + Bicuculine:
#

# ['A_0015', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/22_02_2023/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],
# ['A_0016', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/22_02_2023/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],
# 'SNI_SHAM + PMX205/22_02_2023/A_0017',
# 'SNI_SHAM + PMX205/22_02_2023/A_0018',
# 'SNI_SHAM + PMX205/22_02_2023/A_0019',
#
# 'SNI_SHAM + PMX205/23_02_2023_M1/A_0008',
# 'SNI_SHAM + PMX205/23_02_2023_M1/A_0009',
# 'SNI_SHAM + PMX205/23_02_2023_M1/A_0010',
# 'SNI_SHAM + PMX205/23_02_2023_M1/A_0011',
#
# 'SNI_SHAM + PMX205/23_02_2023_M2/A_0007',
# 'SNI_SHAM + PMX205/23_02_2023_M2/A_0008',
# 'SNI_SHAM + PMX205/23_02_2023_M2/A_0009',
# 'SNI_SHAM + PMX205/23_02_2023_M2/A_0010',
#
# 'SNI_SHAM + PMX205/24_02_2023/A_0015',
# 'SNI_SHAM + PMX205/24_02_2023/A_0016',
# 'SNI_SHAM + PMX205/24_02_2023/A_0017',
# 'SNI_SHAM + PMX205/24_02_2023/A_0018',
#
# 'SNI_SHAM + PMX205/27_02_2023_M1/A_0005',
# 'SNI_SHAM + PMX205/27_02_2023_M1/A_0006',
# 'SNI_SHAM + PMX205/27_02_2023_M1/A_0008',
# 'SNI_SHAM + PMX205/27_02_2023_M1/A_0009',
#
# 'SNI_SHAM + PMX205/27_02_2023_M2/A_0009',
# 'SNI_SHAM + PMX205/27_02_2023_M2/A_0010',
# 'SNI_SHAM + PMX205/27_02_2023_M2/A_0011',
# 'SNI_SHAM + PMX205/27_02_2023_M2/A_0012',
#
# 'SNI_SHAM + PMX205/28_02_2023/A_0001',
# 'SNI_SHAM + PMX205/28_02_2023/A_0002',
# 'SNI_SHAM + PMX205/28_02_2023/A_0003',
# 'SNI_SHAM + PMX205/28_02_2023/A_0004',




# # Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine:
#
# ['A_0001', 
#     {'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_01/',
#     'REFERENCE_FRAME' : 'first'}
# ],
# ['A',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
#     'DISTORTION_TYPE' : 'AFFINE',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],
# ['08_03_2023_0002', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2023_03_08/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],




# # Pirt GCamp3 x Thy1 RGeco + DRS + C5a:

# ['A_0002_0001', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + C5a/2022_12_28/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],




# # TRPV1 Cre x GCamp5g TdT + Capsaicin:
#
# 'TRPV1 Cre x GCamp5g TdT + Capsaicin/06_04_2023_M1/06_04_2023_0003',
# 'TRPV1 Cre x GCamp5g TdT + Capsaicin/06_04_2023_M2/__0001',





# # Organoid project:
#
# ['Organoids/Alzheimer mRuby applications_0001', {'DIRECTORY' : 'F:/Lab Work Files/2-photon/'}],
# 'Organoids/Control mRuby applications_0001',
# ['Organoids/Alzheimer mtRGeco applications_0001', {'DIRECTORY' : 'F:/Lab Work Files/2-photon/'}],
# 'Organoids/Control mtRGeco applications_0001',




# # Microglia + C5a:

# ['Field 4_0001', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Microglia + C5a/25_11_2022/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],



]
