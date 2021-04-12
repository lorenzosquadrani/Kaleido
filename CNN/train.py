# LETS TRY SOME CNN ON OUR LITTLE DRAWINGS

from CNN.neural_networks import squafra_lenet as sfl
import torch as tor
import torch.nn as nn
import math
import numpy as np
import matplotlib.pyplot as plt

def train():
    # Data loading and transformation to tensor
    # Loading the training and test data numpies
    data_circles = np.load('Data/Datasets/training_DrawCircle.npy')
    data_triangles = np.load('Data/Datasets/training_DrawTriangle.npy')
    data = np.concatenate((data_circles,data_triangles),axis=0)

    test_circles = np.load('Data/Datasets/test_DrawCircle.npy')
    test_triangles = np.load('Data/Datasets/test_DrawTriangle.npy')
    test = np.concatenate((test_circles,test_triangles), axis=0)

    # get the resolution of the images and their number
    resolution = len(data[0,0,:,0])
    training_N = len(data[:,0,1,1]) 
    test_N = len(test[:,0,1,1]) 

    # Data tensor construction and NOTE THAT WE CAST TO FLOAT32
    temp = tor.from_numpy(data)
    x_train = temp.to(tor.float)
    temp = tor.from_numpy(test)
    x_test = temp.to(tor.float)

    # Labels construction (tweak the dtype i dunno what does it want)
    y_train = tor.zeros(training_N, dtype=tor.long)
    y_train[(training_N//2):] = 1
    y_test = tor.zeros(test_N, dtype=tor.long)
    y_test[(test_N//2):] = 1

    # CNN call and training
    model = sfl()

    loss_fn = tor.nn.CrossEntropyLoss()
    learning_rate = 1e-3
    optimizer = tor.optim.SGD(model.parameters(),lr=learning_rate)
    nIterations = 10
    lossValues = np.zeros(nIterations) # we use this for the plot later

    # start the loop
    for t in range(nIterations):
        y_pred = model(x_train)
        loss = loss_fn(y_pred,y_train)
        lossValues[t] = loss

        if (t%100 ==0):
            print(f"Iteration {t}: loss = {loss:.2f}")
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # saved the trained parameters
    tor.save(model.state_dict(),'parameters')

    # compute the training accuracy
    guesses = model(x_train)
    max, inds = tor.max(guesses,axis=1)
    correct_train = (y_train == inds).sum()

    # compute the test accuracy
    guesses = model(x_test)
    max, inds = tor.max(guesses,axis=1)
    correct_test = (y_test == inds).sum()

    print(f'Training accuracy = {correct_train/training_N}')
    print(f'Test accuracy = {correct_test/test_N}')

    # show the loss graph
    plt.plot(range(nIterations),lossValues)
    plt.show()