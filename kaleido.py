#!/home/janko/miniconda3/bin/python

import sys
from Data.Generating_algorythms.generator import generator
from Data.Utils.data_viewer import viewData
from CNN.train import train

args = sys.argv[1:]

if (args[0] == 'generate'):
    resolution = int(args[1])
    trainingNumber = int(args[2])
    testNumber = int(args[3])
    gridParams = [[3,5],[1,3]] # ((gauge_min, gauge_max),(width_min, width_max))
    beauty_factor = 0.05 # difference % from empty (see generator.py for more details)

    if ('-g' in args[4:]):
        index = args.index('-g')
        gridParams[0][0] = int(args[index+1])
        gridParams[0][1] = int(args[index+2])

    elif ('--gauge' in args[4:]):
        index = args.index('--gauge')
        gridParams[0][0] = int(args[index+1])
        gridParams[0][1] = int(args[index+2])

    if ('-w' in args[4:]):
        index = args.index('-w')
        gridParams[1][0] = int(args[index+1])
        gridParams[1][1] = int(args[index+2])
    
    elif('--width' in args[4:]):
        index = args.index('--width')
        gridParams[1][0] = int(args[index+1])
        gridParams[1][1] = int(args[index+2])

    if ('-b' in args[4:]):
        index = args.index('-b')
        beauty_factor = float(args[index+1])
    
    elif ('--beauty' in args[4:]):
        index = args.index('--beauty')
        beauty_factor = float(args[index+1])

    generator('training', 'circles', resolution, trainingNumber, gridParams, beauty_factor)
    generator('training', 'triangles', resolution, trainingNumber, gridParams, beauty_factor)
    generator('test', 'circles', resolution, testNumber, gridParams, beauty_factor)
    generator('test', 'triangles',resolution, testNumber, gridParams, beauty_factor)

    print('\n Training and test datasets generated succesfully.\n You can now:')
    print(' - view some dataset items with with $ kaleido view')
    print(' - traing the neural network with $ kaleido train\n')


if (args[0] == 'view_data'):
    viewData()


if (args[0] == 'train'):
    train()
    
    
'''
    print(f'Generating {datasetType} dataset with {drawFunction.__name__}.')
    print(f"    Number of figures to be generated: {figNumber}")
    print(f"    Number of channels: 1")
    print(f"    Figure resolution: {resolution} x {resolution}\n")
    print(f"    Grid gauge: {gridParams[0,0]}-{gridParams[0,1]}")
    print(f"    Grid width: {gridParams[1,0]}-{gridParams[1,1]}")
'''
