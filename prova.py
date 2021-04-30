from Data.Utils.custom_dataset import CustomDataset as CD
import matplotlib.pyplot as plt

# prova della classe custom_dataset
dataset = CD('Data/Datasets','training')

#__GetItem__(index)
sample = dataset[4]
print(type(sample['image']),type(sample['label']))


