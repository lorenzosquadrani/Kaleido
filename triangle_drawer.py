import numpy as np
import matplotlib.pyplot as plt


# auxiliary functions for drawing straight edges between 2 points
def getB(P,Q):
    payload = (Q[1]-P[1])/(Q[0]-P[0])
    return payload

def getAFromB(P,b):
    payload = P[1] - b*P[0]
    return payload

# we suppose y = a + bx
def getBA(P,Q):
    payload = [0,0]
    payload[1] = getB(P,Q)
    payload[0] = getAFromB(P,payload[1])
    return payload
    

# draw a payload over (1) or under (0) a square grating.
# cscheme: black triangle on white sfondo (1) or opposite (0)

def drawTriangle(resolution,position,cscheme):
    imgDim = 150 # image format is imgDim x imgDim
    nVertices = 3 # number of polygon vertices 

    # generate coordinates sorted from left to right
    coords = np.random.randint(0,imgDim-1, (nVertices,2))
    coords = np.sort(coords, axis=0)

    # how is the orientation of the points
    helicity = (coords[2,1] > ((coords[1,1]-coords[0,1])/(coords[1,0]-coords[0,0])*(coords[2,0]-coords[0,0])))
    helicity = 2*helicity - 1 # this is just some bs to get helicity +- 1

    # define the three straight line equations
    params = np.zeros((3,2))
    params[0,:] = getBA(coords[0,:],coords[1,:])
    params[1,:] = getBA(coords[1,:],coords[2,:])
    params[2,:] = getBA(coords[2,:],coords[0,:])


    # draw the payload (very stupid way)
    payload = np.zeros((imgDim, imgDim))

    if (position):
        payload[0:imgDim:20,:] = 0.5
        payload[1:imgDim:20,:] = 0.5
        payload[2:imgDim:20,:] = 0.5
        payload[3:imgDim:20,:] = 0.5
        payload[:,0:imgDim:20] = 0.5
        payload[:,1:imgDim:20] = 0.5
        payload[:,2:imgDim:20] = 0.5
        payload[:,3:imgDim:20] = 0.5

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


    if (not(position)):
        payload[0:imgDim:20,:] = 0.5
        payload[1:imgDim:20,:] = 0.5
        payload[2:imgDim:20,:] = 0.5
        payload[3:imgDim:20,:] = 0.5
        payload[:,0:imgDim:20] = 0.5
        payload[:,1:imgDim:20] = 0.5
        payload[:,2:imgDim:20] = 0.5
        payload[:,3:imgDim:20] = 0.5

    if (cscheme):
        payload = -2*payload+1
    
    return payload


triangle = drawTriangle(50,0,0)
plt.imshow(triangle, cmap='gray')
plt.show()