import numpy as np
import figgen_draw_functions as fdf
import matplotlib.pyplot as plt


# This guy creates a dataset matrix of dimension figNumber x resolution^2 using the
# using the "drawFunction" method

# GENERATION PARAMETERS
figNumber = 1000  # how many figures do you want to draw
drawFunction = fdf.DrawCircle # which polygon do you want to draw
resolution = 100 # pixels in one dimension
gridParams = ((10,20),(3,6)) # ((gauge_min, gauge_max),(width_min, width_max))
#foreground_white = np.random.randint(0,2,2) # fg vs bg / wb vs bw. For now we keep it random
beauty = resolution*resolution/150 # how different is the generated figure from an empty grid


print(f"Number of figures to be generated: {figNumber}")
print(f"Draw function: {drawFunction.__name__}")
print(f"Figure resolution: {resolution} x {resolution}\n")

print("Commencing...")

# Generation loop: each iteration inserts a 1 x resolution row in the starting empty
# dataset matrix
data = np.zeros((figNumber,resolution*resolution))
for i in range(figNumber):
    foreground_white = np.random.randint(0,2,2) # we put it here because we want it random
    
    # draw image, reshape and add
    figure = fdf.GenerateFigure(drawFunction,resolution,gridParams,foreground_white,beauty)
    figure = figure.reshape((1,-1)).copy()
    data[i,:] = figure
    
    # little update every now and then
    if (i%(figNumber//10)==0):
        print(f"Generated figures: {i}")

print("...done!.\n")
print("Saving data matrix...", end="" )
np.save(f'./data_{drawFunction.__name__}',data)
print("saved.")


'''
THIS WILL BE USEFUL FOR THE GRAPHICAL PARSER I THINK

# Generation loop: each iteration glues a square matrix to the right side of one big
# global matrix. The final dimension will therefore be resolution*(figNumber x 1)
finalFigure = np.zeros((resolution,figNumber*resolution))
for i in range(figNumber):
    _frame = i*resolution
    frame_ = (i+1)*resolution
    figure = fdf.GenerateFigure(drawFunction,resolution,gridParams,foreground_white,beauty)
    finalFigure[:,_frame:frame_]= figure
    


plt.imshow(finalFigure, cmap='gray')
plt.show()
'''