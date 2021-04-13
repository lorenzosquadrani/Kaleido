#!/home/janko/miniconda3/bin/python -B

import sys
from Data.Generating_algorythms.generator import generator
from Data.Utils.data_viewer import viewData
from CNN.train import train
import IL
import numpy as np

args = sys.argv[1:]

if (args[0] == 'generate'):
    resolution = int(args[1])
    trainingNumber = int(args[2])
    testNumber = int(args[3])
    gridParams = [[3,5],[1,3]] # ((gauge_min, gauge_max),(width_min, width_max))
    beauty_factor = 0.05 # difference % from empty (see generator.py for more details)

    # chech the mode options
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

    # construct cubic tensor + labels for the training
    print("\n ### Generating the training figures...")
    print("-------------------------------")
    i = 0
    training_figures = np.zeros((trainingNumber*len(IL.figures),resolution,resolution))
    training_labels = np.zeros(trainingNumber*len(IL.figures))
    for figure in IL.figures:
        temp = generator('training', figure, resolution, trainingNumber, gridParams, beauty_factor)
        training_figures[i*trainingNumber:(i+1)*trainingNumber] = temp
        training_labels[i*trainingNumber:(i+1)*trainingNumber] = i   
        i+=1

    np.save("Data/Datasets/training_figures.npy", training_figures)
    np.save("Data/Datasets/training_labels.npy", training_labels)
    print(f"...training figures generation succesful, tensor shape {training_figures.shape} ###")

    # construct cubic tensor + labels for the test
    print("\n\n ### Generating the test figures...")
    print("-------------------------------")
    i = 0
    test_figures = np.zeros((testNumber*len(IL.figures),resolution,resolution))
    test_labels = np.zeros(testNumber*len(IL.figures))
    for figure in IL.figures:
        temp = generator('test', figure, resolution, testNumber, gridParams, beauty_factor)
        test_figures[i*testNumber:(i+1)*testNumber] = temp
        test_labels[i*testNumber:(i+1)*testNumber] = i
        i+=1

    np.save("Data/Datasets/test_labels.npy", test_labels)
    np.save("Data/Datasets/test_figures.npy", test_figures)
    print(f"...test figures generation succesful, tensor shape {test_figures.shape} ###")
    

    print('\n You can now:')
    print(' - $ kaleido view_data')
    print(' - $ kaleido train\n')


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
