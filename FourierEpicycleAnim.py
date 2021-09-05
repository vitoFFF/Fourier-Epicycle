import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

ammpllist = [12,9,6,3,1,0.5,0.02,0.01,0.005]
phasseList = [0,0,0,0,0,0,0,0,0]
freqllist = [0.5,1,3,6,7,8,9,11,12]

def animate(theta_time):
    ax.cla()
    C_x = 0
    C_y = 0
    cx = [0]
    cy = [0]

    for freq,amp,phase in zip(freqllist,ammpllist, phasseList):
        circle = plt.Circle((C_x, C_y), amp, fill = False)
        ax.add_patch(circle)
        C_x += amp*np.cos(freq * theta_time + np.deg2rad(phase))
        C_y += amp*np.sin(freq * theta_time + np.deg2rad(phase))
        cx.append(C_x)
        cy.append(C_y)
    ax.scatter(cx,cy)
    ax.plot(cx, cy, '.r-',linewidth=1)
    ax.set_xlim(-34, 34)
    ax.set_ylim(-34, 34)
    #ax.set_title(r'$\theta_{time} = $' + str(theta_time))
fig, ax = plt.subplots(figsize = (8, 8))
ani = FuncAnimation(fig = fig, func = animate,frames=np.arange(0,6.28,1/60),interval=1)
plt.show()
