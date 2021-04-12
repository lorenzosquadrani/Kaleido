import numpy as np
import matplotlib.pyplot as plt
from . import head_draw_functions as hdf
from ..Utils.IL import IL


# This guy creates a dataset matrix of dimension resolution x resolution x figNumber using the
# using the "drawFunction" method
def generator(
    datasetType,
    figure, # which figure are we drawing the dataset with
    resolution, # pixels in one dimension
    figNumber,  # how many figures do you want to draw
    gridParams, # ((gauge_min, gauge_max),(width_min, width_max))
    beauty_factor
    #foreground_white = np.random.randint(0,2,2) # fg vs bg / wb vs bw. For now we keep it random
):
    # first retrieve the name of the function to be used to generate
    drawFunction = IL[figure]

    # Beauty is the minimum number of pixels that has to be different between the generated image
    # and an empty grid (see the code to understand). So with a factor of 0.1 we can accept
    # generated images that are at least 10% different from an empty grid. Basically, the more
    # beautiful the easier it is for the CNN to spot the figure.
    beauty = int(resolution*resolution*beauty_factor)

    # Print chosen parameters
    print(f'\n # Generating {datasetType} dataset with {drawFunction.__name__} function.')
    print(f"    Number of figures to be generated: {figNumber}")
    print(f"    Number of channels: 1")
    print(f"    Figure resolution: {resolution} x {resolution}")
    print(f"    Grid gauge: {gridParams[0][0]}-{gridParams[0][1]}")
    print(f"    Grid width: {gridParams[1][0]}-{gridParams[1][1]}")
    print(f"    Beauty: {beauty} px\n")
    
    

    
    # Generation loop: each iteration inserts a resolution x resolution x 1 dish in the starting empty
    # dataset "cube". The explicit additional dimension 1 serves later purpose in the CNN
    print("    Commencing", end="")
    
    data = np.zeros((figNumber, 1, resolution,resolution))
    for i in range(figNumber):
        foreground_white = np.random.randint(0,2,2) # we put it here because we want it random
        
        # draw image, reshape and add
        temp = hdf.GenerateFigure(drawFunction,resolution,gridParams,foreground_white,beauty)
    
        # add additional dimension at axis 0 (prolly there is a better way to do it)
        temp = np.expand_dims(temp,axis=2)
        figure = temp.transpose(2,0,1)
        # add to the data matrix
        data[i,:,:,:] = figure
        
        # little update every now and then
        if (i%(figNumber//10)==0):
            print(f".", end="")
    
    print("...done!.")
    print("    Saving data matrix...", end="" )
    np.save(f'Data/Datasets/{datasetType}_{drawFunction.__name__}.npy',data)
    print("saved.")
    
