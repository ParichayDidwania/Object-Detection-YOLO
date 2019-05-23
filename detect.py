import cv2
import tensorflow as tf
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import os

# define the model options and run
script_dir = os.path.dirname(__file__)
options = {
    'model': 'cfg/tiny-yolo-voc-10c.cfg',
    'load': 61703,
    'threshold': 0.02,
    'gpu': 1.0
}

tfnet = TFNet(options)

img = cv2.imread('C:/Users/default.DESKTOP-43PHGMT/Downloads/car1.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


result = tfnet.return_predict(img)

max=0
for i in range(len(result)):
    if(result[i]['confidence']>max):
        max=result[i]['confidence']
        tl1 = (result[i]['topleft']['x'], result[i]['topleft']['y'])
        br1 = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
        label = result[i]['label']

print(max)
print(result)
print(tl1,br1)


# add the box and label and display it
img = cv2.rectangle(img, tl1, br1, (0, 255, 0), 3)

img = cv2.putText(img, label, tl1, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
plt.imshow(img)
plt.show()

