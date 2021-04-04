# AUXILIARY FUNCTIONS

# Get straight line parameters, supposing y = a +bx

def GetB(P,Q):
    payload = (Q[1]-P[1])/(Q[0]-P[0])
    return payload

def GetAFromB(P,b):
    payload = P[1] - b*P[0]
    return payload

def GetBA(P,Q):
    payload = [0,0]
    payload[1] = GetB(P,Q)
    payload[0] = GetAFromB(P,payload[1])
    return payload

#####