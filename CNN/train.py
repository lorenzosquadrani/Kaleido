import matplotlib.pyplot as plt
import numpy as np

import torch
import torch.nn as nn
import torchvision

import torch.optim as optim

from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

from Data.Utils.custom_dataset import CustomDataset as CD
from CNN.custom_networks import squafra_lenet as sql

def train():
    training_dataset = CD('Data/Datasets','training')
    test_dataset = CD('Data/Datasets','test')

    training_loader = DataLoader(training_dataset, batch_size=16, shuffle=True,num_workers=2)


    # writer = SummaryWriter('Runs/boundary_completion_run')

    model = sql()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.SGD(model.parameters(), lr=1e-3, momentum=0)    
    
    # get some random training images
    writer = SummaryWriter('Runs/prova')
    dataiter = iter(training_loader)

    images, labels = dataiter.next()

    img_grid = torchvision.utils.make_grid(images)
    plt.imshow(img_grid)
    writer.add_image('prova',img_grid)