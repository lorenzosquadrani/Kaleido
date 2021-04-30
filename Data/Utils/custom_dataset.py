import torch as tor
from torch.utils.data import Dataset
import numpy as np

class CustomDataset(Dataset):
    def __init__(self,path_to_folder,datasetType):
        self.figures = np.load(f'{path_to_folder}/{datasetType}_figures.npy')
        
        self.n_samples = (self.figures).shape[0]
        self.sample_width = (self.figures).shape[1]
        self.sample_heigth = (self.figures).shape[2]
        
        self.labels = np.load(f'{path_to_folder}/{datasetType}_labels.npy')

    def __len__(self):
        return (self.n_samples)

    def __res__(self):
        return len(self.figures[0,:,0])
    
    def __getitem__(self,index):
        if tor.is_tensor(index):
            index = index.tolist()

        image = tor.from_numpy(self.figures[index,:,:].reshape(1, self.sample_width, self.sample_heigth))
        label = int(self.labels[index].item())

        return image, label