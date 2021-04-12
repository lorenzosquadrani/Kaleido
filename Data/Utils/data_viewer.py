# THIS THING IS NOT GENERALIZED, IT NEEDS BOTH CIRCLES AND TRIANGLES, BOTH TEST AND TRAINING
# Data visualizer: basically just takes the data cubes, loads them, tells the 
# useful data features (resolution, number of elements...) and shows some pics
# if you like it to

import numpy as np
import matplotlib.pyplot as plt

def viewData():
    # load the good good
    training_dataset = np.load('Data/Datasets/training_dataset.npy')
    test_dataset = np.load('Data/Datasets/test_dataset.npy')

    # print out some useful information
    print('\n Circles training dataset')
    print('----------------------')
    print(f"    Number of figures: {len(trainingCircles[:,0,0,0])}")
    print(f"    Channels: {len(trainingCircles[0,:,0,0])}")
    print(f"    Figure resolution: {len(trainingCircles[0,0,:,0])} x {len(trainingCircles[0,0,:,0])}\n")

    print('\n Triangles training dataset')
    print('----------------------')
    print(f"    Number of figures: {len(trainingTriangles[:,0,0,0])}")
    print(f"    Channels: {len(trainingTriangles[0,:,0,0])}")
    print(f"    Figure resolution: {len(trainingTriangles[0,0,:,0])} x {len(trainingTriangles[0,0,:,0])}\n")

    print('\n Circles test dataset')
    print('----------------------')
    print(f"    Number of figures: {len(testCircles[:,0,0,0])}")
    print(f"    Channels: {len(testCircles[0,:,0,0])}")
    print(f"    Figure resolution: {len(testCircles[0,0,:,0])} x {len(testCircles[0,0,:,0])}\n")

    print('\n Triangles test dataset')
    print('----------------------')
    print(f"    Number of figures: {len(testTriangles[:,0,0,0])}")
    print(f"    Channels: {len(testTriangles[0,:,0,0])}")
    print(f"    Figure resolution: {len(testTriangles[0,0,:,0])} x {len(testTriangles[0,0,:,0])}\n")

    print('\n Showing a couple photos from the sets')

    # add something to visualize this pics
    training_circle = np.random.random_integers(0,len(trainingCircles[:,0,0,0])-1)
    training_triangle = np.random.random_integers(0,len(trainingTriangles[:,0,0,0])-1)
    test_circle = np.random.random_integers(0,len(testCircles[:,0,0,0])-1)
    test_triangle = np.random.random_integers(0,len(testTriangles[:,0,0,0])-1)


    fig = plt.figure()

    fig.add_subplot(4,2,1)
    plt.imshow(trainingCircles[training_circle,0,:,:], cmap='gray')
    fig.add_subplot(4,2,2)
    plt.imshow(trainingCircles[training_circle+1,0,:,:], cmap='gray')

    fig.add_subplot(4,2,3)
    plt.imshow(trainingTriangles[training_triangle,0,:,:], cmap='gray')
    fig.add_subplot(4,2,4)
    plt.imshow(trainingTriangles[training_triangle+1,0,:,:], cmap='gray')

    fig.add_subplot(4,2,5)
    plt.imshow(testCircles[test_circle,0,:,:], cmap='gray')
    fig.add_subplot(4,2,6)
    plt.imshow(testCircles[test_circle+1,0,:,:], cmap='gray')

    fig.add_subplot(4,2,7)
    plt.imshow(testTriangles[test_triangle,0,:,:], cmap='gray')
    fig.add_subplot(4,2,8)
    plt.imshow(testTriangles[test_triangle+1,0,:,:], cmap='gray')


    plt.show()