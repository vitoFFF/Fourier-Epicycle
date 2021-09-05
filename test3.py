import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import matplotlib.animation as animation

ampList = [6,4,2,1,0.2]
phaseList = [0,0,0,0,0]
freqList = [6,4,3,2,0.1]
fig, ax = plt.subplots()
C_x = 0
C_y = 0

#for lines
cx = [0]
cy = [0]
theta_time = 0

for freq,amp, phase in zip(freqList,ampList, phaseList):
    theta_time+=1
    circle = plt.Circle((C_x, C_y), amp, fill = False)
    ax.add_patch(circle)
    C_x += amp*np.cos(freq * theta_time + np.deg2rad(phase))
    C_y += amp*np.sin(freq * theta_time + np.deg2rad(phase))
    cx.append(C_x)
    cy.append(C_y)

plt.scatter(cx,cy)
plt.plot(cx, cy, '.r-',linewidth=1)    
plt.axis("equal")
plt.xlim( -20 , 20 )
plt.ylim( -20 , 20 )
plt.show()