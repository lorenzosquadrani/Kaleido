import torch.nn as nn
from torch import flatten

class squafra_lenet(nn.Module):
    def __init__(self):
        super().__init__() 
                                                                           #input 1x28x28
        self.conv1 = nn.Conv2d(1,8,kernel_size = 5 , stride = 1, padding = 0)      #8x24x24
        self.batch1 = nn.BatchNorm2d(8, track_running_stats=False)
        self.drop1 = nn.Dropout(0.1)

        self.pool1 = nn.MaxPool2d(kernel_size=3, stride=3)                          #8x8x8
 
        self.conv2 = nn.Conv2d(8,16, kernel_size = 5 , stride = 1 , padding = 0)        #4x4x16
        self.batch2 = nn.BatchNorm2d(16, track_running_stats=False)
        self.drop2 = nn.Dropout(0.1)

        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2 )                     #16x2x2

        self.linear1 = nn.Linear(2*2*16, 128)
        self.linear2 = nn.Linear(128,2)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.conv1(x)
        out = self.batch1(out)
        out = self.drop1(out)
        out = self.relu(out)
        out = self.pool1(out)

        out = self.conv2(out)
        out = self.batch2(out)
        out = self.drop2(out)
        out = self.relu(out)
        out = self.pool2(out)

        out = flatten(out,1)

        out = self.linear1(out)
        out = self.relu(out)
        out = self.linear2(out)
        return out



class tweaked_squafra(nn.Module):
    def __init__(self):
        super().__init__() 
        self.conv1 = nn.Conv2d(1,8,kernel_size=5,stride=1,padding=0) # in 1x28x28
        self.conv2 = nn.Conv2d(8,16,kernel_size=5,stride=1,padding=0) # in 8x24x24
        self.linear1 = nn.Linear(20*20*16,10) 
        self.linear2 = nn.Linear(10,2)
        self.relu = nn.ReLU()

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = flatten(out,1)
        out = self.linear1(out)
        out = self.relu(out)
        out = self.linear2(out)
        return out