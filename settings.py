#!/usr/bin/env python3
################################# Settings block:


DIRECTORY = "F:/Lab Work Files/2-photon/" # 'data/'
                                # Provide full path to files. Leave quotes empty if the files in the same directory with this script

DISTORTION_TYPE = 'BILINEAR'
                                # TRANSLATION        - translation
                                # RIGID_BODY         - translation + rotation
                                # SCALED_ROTATION    - translation + rotation + scaling
                                # AFFINE             - translation + rotation + scaling + shearing
                                # BILINEAR           - non-linear transformation (no support for 'previous' reference frame mode)

REFERENCE_FRAME = 'first'
                                # first, previous, mean

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

MULTIPROCESSING = True
                                # Use all available CPU cores.
                                # Faster, but need much more RAM so can be unstable.


TODO_LIST = [                   # list here quoted TIFF file names without .tiff extensions, separated by comma:


# # TRP project

# ['Field 1_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M1/',
#     'DISTORTION_TYPE' : 'TRANSLATION',
#     'REFERENCE_FRAME' : 'previous',
#     'REFERENCE_CHANNEL' : 1, 
#     'NUMBER_OF_REF_FRAMES' : 1,
#     'MOVING_AVERAGE' : 1,
#     }
# ],
# ['Field 1_0001_ch1_registered',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M1/',
#     'DISTORTION_TYPE' : 'TRANSLATION',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 1, 
#     'NUMBER_OF_REF_FRAMES' : 20,
#     'MOVING_AVERAGE' : 40,
#     }
# ],
# ['Field 1_0001_ch2_registered',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M1/',
#     'DISTORTION_TYPE' : 'TRANSLATION',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 1, 
#     'NUMBER_OF_REF_FRAMES' : 20,
#     'MOVING_AVERAGE' : 40,
#     }
# ],

# ['Field 1_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M2/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ],
# ['Field 1_0001_ch2_registered_',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2023_12_22_M2/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ],

# ['Field_1',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ],
# ['Field_2_0001_DRS_part',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ],
# ['Field_2_0001_drug_part',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_02_M3/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 20,
#     'MOVING_AVERAGE' : 60,
#     }
# ],
# ['Field_1',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_05_M4/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 20,
#     'MOVING_AVERAGE' : 60,
#     }
# ],
# ['Field_2_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/TRP project Ca-imaging with DRS + TRPC3, TRPA1, TRPM3 activators + Caps/2024_02_05_M4/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'REFERENCE_CHANNEL' : 0, 
#     'NUMBER_OF_REF_FRAMES' : 20,
#     'MOVING_AVERAGE' : 60,
#     }
# ],





# # MCU-KO project:
# # Pirt_GCamp3 x MCU-KO + DRS + Caps:

# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/4 A+C and C - 0.1 Hz',
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/5 A+C and C - 0.1 Hz',
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/6 A+C and C - 0.1 Hz_0001',
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/7',
# ['8_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M1/',
#     'DISTORTION_TYPE' : 'AFFINE',
#     'REFERENCE_FRAME' : 'previous',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ]



# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_24_M2/3_0001',

# ['2',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ]
# ['3',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ]
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/4',
# ['6_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M3/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ]

# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M4/1_0000',
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M4/1_0001',
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_26_M4/2_0001',

# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_30_M5/1_0000',
# ['1_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_30_M5/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ]
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_10_30_M5/3_0001',

# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_01_M6/2',
# ['3',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_01_M6/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ]
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_01_M6/5_0001',

# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_02_M7/1',

# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_03_M8/1_0000',
# ['1_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_03_M8/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 30,
#     }
# ]
# 'Pirt_GCamp3 x MCU-KO + DRS + Caps/2023_11_03_M8/1_0002',



# # C5a complement project:
# # Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS + PMX205 + Bicuculine:
#

# ['A_0015', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/22_02_2023/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
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
# ['A_0008', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco SNI or SHAM + DRS  + PMX205 + Bicuculine/23_02_2023_M2/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ],

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
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_01/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
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
# ['A_0001',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ],
# ['A_0003',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ],
# ['A_0004',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_14/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ],    
# ['A_0003',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_05/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 10,
#     }
# ],
# ['A_0005',
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2022_12_09/',
#     'DISTORTION_TYPE' : 'BILINEAR',
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
# ['09_03_2023_0002', 
#     {
#     'DIRECTORY' : 'F:/Lab Work Files/2-photon/Pirt GCamp3 x Thy1 RGeco + DRS + Bicuculine/2023_03_09/',
#     'DISTORTION_TYPE' : 'BILINEAR',
#     'REFERENCE_FRAME' : 'first',
#     'NUMBER_OF_REF_FRAMES' : 10,
#     'MOVING_AVERAGE' : 20,
#     }
# ],






# # C5a complement project:
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









# # C5a complement project:
# # Microglia + C5a:

# 'Microglia + C5a/21_11_2022/B_0002',
# 'Microglia + C5a/21_11_2022/C_0002',
# 'Microglia + C5a/21_11_2022/D_0001',
# 'Microglia + C5a/21_11_2022/E_0002',
# 'Microglia + C5a/21_11_2022/E_0003',

# 'Microglia + C5a/24_11_2022/Field 11',

# 'Microglia + C5a/25_11_2022/Field 4_0001',
# 'Microglia + C5a/25_11_2022/Field 7_0001',

# 'Microglia + C5a/2023_11_17/1_0000',
# 'Microglia + C5a/2023_11_17/4_0001',

# 'Microglia + C5a/2023_11_20/B',
# 'Microglia + C5a/2023_11_20/C_0001',
# 'Microglia + C5a/2023_11_20/D_0001',
# ['E_0001', {'DIRECTORY' : 'F:/Lab Work Files/2-photon/Microglia + C5a/2023_11_20/', 'DISTORTION_TYPE' : 'BILINEAR', 'REFERENCE_FRAME' : 'first', 'REFERENCE_CHANNEL' : 2, 'NUMBER_OF_REF_FRAMES' : 20, 'MOVING_AVERAGE' : 20,}],

# 'Microglia + C5a/2023_11_21/A_overview_3_0001',
# 'Microglia + C5a/2023_11_21/C_0002',
# 'Microglia + C5a/2023_11_21/D',
# 'Microglia + C5a/2023_11_21/F',
# 'Microglia + C5a/2023_11_21/G_0001',


]



if __name__ == '__main__':
    import stackreg
    stackreg.main()