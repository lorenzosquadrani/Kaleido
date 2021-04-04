import head_auxiliary as aux
import numpy as np
import math
    

# DRAW A TRIANGLE: random white triangle on a black background
def DrawTriangle(resolution):
    # generate coordinates sorted from left to right
    coords = np.random.randint(0,resolution, (3,2))
    coords = np.sort(coords, axis=0)

    # how is the "orientation" of the points
    helicity = (coords[2,1] > ((coords[1,1]-coords[0,1])/(coords[1,0]-coords[0,0])*(coords[2,0]-coords[0,0])))
    helicity = 2*helicity - 1 # this is just some bs to Get helicity +- 1

    # define the three straight line equations
    params = np.zeros((3,2))
    params[0,:] = aux.GetBA(coords[0,:],coords[1,:])
    params[1,:] = aux.GetBA(coords[1,:],coords[2,:])
    params[2,:] = aux.GetBA(coords[2,:],coords[0,:])

    # draw the payload with Darboux-Riemann (can't come up with anything better)
    payload = np.zeros((resolution, resolution))

    for i in range(coords[0,0],coords[1,0]):
        jMin = helicity*(params[0,0]+i*params[0,1]).astype(int)
        jMax = helicity*(params[2,0]+i*params[2,1]).astype(int)
        for j in range(jMin,jMax):
            payload[i,j]=1

    for i in range(coords[1,0],coords[2,0]):
        jMin = helicity*(params[1,0]+i*params[1,1]).astype(int)
        jMax = helicity*(params[2,0]+i*params[2,1]).astype(int)
        for j in range(jMin,jMax):
            payload[i,j]=1
    
    return payload


# DRAW A CIRCLE: random white circle on black background
def DrawCircle(resolution):
    payload = np.zeros((resolution, resolution))

    # generate random center position and compatible radius (0% sure this is the best way)
    centerCoords = np.random.randint(0,resolution,2)
    rmax = min(centerCoords[0],centerCoords[1],resolution-centerCoords[0], resolution-centerCoords[1])
    
    if (rmax == 0): # a little check that our radius can be bigger than 0
        return payload # if not, return an empty square that will be discarded later

    radius = np.random.randint(0,rmax) # this is awkward but im not importing random

    # draw the circle with the Darboux-Riemann
    imin = centerCoords[0]-radius+1
    imax = centerCoords[0]+radius

    for i in range(imin,imax):
        jlim = np.sqrt(radius*radius-(i-centerCoords[0])*(i-centerCoords[0])).astype(int)
        #jlim = rmax
        for j in range(centerCoords[1]-jlim, centerCoords[1]+jlim):
            payload[i,j] = 1

    return payload


# DRAW A GRID PATTERN: creates a white grid pattern on black background; grid
# parameters such as gauge and stripe width are drawn from a user defined 
# interval
def DrawGrid(resolution,gridParams):
    # create grid matrix
    payload = np.zeros((resolution,resolution))

    # define random grid parameters:
    #   stripeGauge = (x_spacing, y_spacing)
    #   stripeWidth = (x_width, y_width)
    stripeGauge = np.random.randint(gridParams[0][0],gridParams[0][1],2)
    stripeWidth = np.random.randint(gridParams[1][0],gridParams[1][1],2)

    # draw the grid from the params
    for i in range(stripeWidth[0]):
        payload[i:resolution:stripeGauge[0],:] = 1
    for i in range(stripeWidth[1]):
        payload[:,i:resolution:stripeGauge[1]] = 1

    return payload




# GENERATE THE FINAL FIGURE
# calls one polygon drawer and the grid drawer, combining them together. Checks then if 
# the obtained figure is sufficiently beautiful (different from an empty grid) and in
# case it is not, generates again.
def GenerateFigure(DrawFunction, resolution, gridParams, foreground_white, beauty):

    payload = np.zeros(1)
    _ = True
    
    while _:
        # Draw payload and grid
        payload = DrawFunction(resolution)
        gridMask = DrawGrid(resolution,gridParams)

        # Mask the payload
        if (foreground_white[0]): #foreground
            payload = (payload+0.5*gridMask).clip(0,1)
        else: # background
            payload = (payload-gridMask).clip(0,1)+0.5*gridMask

        # Check if the generation is  a e s t h e t i c
        beautiful = (payload-0.5*gridMask).sum()
        if (beautiful > beauty):
            _ = False                                                   # LOOP EXIT CONDITION

        # black payload on white background
        if (not(foreground_white[1])):
            payload = 1-payload

    return payload