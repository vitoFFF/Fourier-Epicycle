import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from scipy.fftpack import fft, ifft

ammpllist = [12,9,6,3,1,0.5,0.02,0.01,0.005]
phasseList = [0,0,0,0,0,0,0,0,0]
freqllist = [0.5,1,3,6,7,8,9,11,12]

# data = [complex(i, i) for i in range(10)] 

# data1 = [(-239-241j), (-239-141j), (-239-41j), (-239-59j), (-239-159j), (-218-239j),
# (-118.5+239j), (-18.5+239j), (81.5+239j), (181.5+239j), (241+198.5j), (241+98.5j), (241-1.5j), (241-101.5j),
# (241-201.5j),(180-241j),(80-241.5j),(-20-241j),(-220-241.5j)]

# data1_x = [-239., -239., -239., -239., -239., -218.5, -118.5, -18.5, 81.5,
# 181.5, 241., 241., 241., 241., 241., 180., 80., -20., -120., -220.]

# data_y = [-241., -141., -41., 59., 159., 239., 239., 239., 239., 239., 198.5,
# 98.5, -1.5, -101.5, -201.5, -241., -241., -241., -241., -241.]

# dftList = fft(data1)
# freqList = []
# ampList = []
# phaseList = []
# print(data)
# for k in range(5):
#     freq = k
#     amp = np.sqrt(dftList[k].real * dftList[k].real + dftList[k].imag * dftList[k].imag) 
#     phase = np.arctan2(dftList[k].real,dftList[k].imag)
#     ampList.append(amp)
#     freqList.append(freq)
#     phaseList.append(phase)



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
