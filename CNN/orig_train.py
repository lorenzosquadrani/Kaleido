# LETS TRY SOME CNN ON OUR LITTLE DRAWINGS

from torch.utils.data import DataLoader
from Data.Utils.custom_dataset import CustomDataset as CD
from CNN.neural_networks import squafra_lenet as sfl
import torch as tor
import torch.nn as nn
import math
import numpy as np
import matplotlib.pyplot as plt

def train():
    # Load the data and create the datasets
    training_data = CD('Data/Datasets','training')
    test_data = CD('Data/Datasets','test')

    train_dataloader = DataLoader(training_data,batch_size=64,shuffle=True)
    
    model = sfl()
    loss_fn = tor.nn.CrossEntropyLoss()
    learning_rate = 1e-3
    optimizer = tor.optim.SGD(model.parameters(),lr=learning_rate)
    nIterations = 10
    
    lossValues = np.zeros(nIterations) # we use this for the plot later

    # start the loop
    for t in range(nIterations):
        y_pred = model(train_dataloader)
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
    guesses = model(test_data)
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