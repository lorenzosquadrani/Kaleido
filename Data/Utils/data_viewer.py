# THIS THING IS NOT GENERALIZED, IT NEEDS BOTH CIRCLES AND TRIANGLES, BOTH TEST AND TRAINING
# Data visualizer: basically just takes the data cubes, loads them, tells the 
# useful data features (resolution, number of elements...) and shows some pics
# if you like it to

import numpy as np
import matplotlib.pyplot as plt

def viewData():
    # load the good good
    training_figures = np.load('Data/Datasets/training_figures.npy')
    training_labels = np.load('Data/Datasets/training_labels.npy')
    test_figures = np.load('Data/Datasets/test_figures.npy')
    test_labels = np.load('Data/Datasets/test_labels.npy')

    # print out some useful information about the training set
    print('\n #  Training dataset')
    print('----------------------')
    print(f"    Figure number: {len(training_figures[:,0,0])}")
    print(f"    Figure resolution: {len(training_figures[0,0,:])} x {len(training_figures[0,0,:])}")
    print(f"    Figure type number {training_labels.max()}")

    # print out some useful information about the test set
    print('\n #  Test dataset')
    print('----------------------')
    print(f"    Figure number: {len(test_figures[:,0,0])}")
    print(f"    Figure resolution: {len(test_figures[0,0,:])} x {len(test_figures[0,0,:])}")
    print(f"    Figure type number {test_labels.max()}")

    print('\n Showing a couple photos from the sets')

    # add something to visualize these pics
    training_extraction = np.random.random_integers(0,len(training_figures[:,0,0])-1, 5)
    test_extraction= np.random.random_integers(0,len(test_figures[:,0,0])-1,5)

    fig = plt.figure()

    k = 1
    for i in training_extraction:
        fig.add_subplot(2,5,k)
        plt.imshow(training_figures[i,:,:], cmap='gray')
        k += 1

    for i in test_extraction:
        fig.add_subplot(2,5,k)
        plt.imshow(test_figures[i,:,:], cmap='gray')
        k += 1

    plt.show()
