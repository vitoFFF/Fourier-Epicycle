import numpy as np
import matplotlib.pyplot as plt
import PIL
from PIL import Image
from IPython.display import HTML
from matplotlib import animation, rc
from scipy.integrate import quad
import cv2

file = "C:/Users/vitok/Desktop/FourierPython/pi.jpg"
img = cv2.imread(file)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
contours = np.array(contours[1]) 

x_list, y_list = contours[:, :, 0], -contours[:, :, 1]
x_list, y_list = contours[:, :, 0].reshape(-1,), -contours[:, :, 1].reshape(-1,)
print(x_list.shape)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_list, y_list)
plt.show()

# Displaying the image 
#cv2.imshow('image',img_gray)


#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
cv2.destroyAllWindows() 