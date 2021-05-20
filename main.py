import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt
import numpy as np

options = {
    'model': 'yolov2-tiny.cfg',
    'load': 'yolov2-tiny_2000.weights',
    'threshold': 0.15,
    'gpu': 1.0
}

tfnet = TFNet(options)
img = cv2.imread('Images/7.jpg')
result = tfnet.return_predict(img)
iz = 0
Ap = 0
count = 0
print('#############  Diameter of Zones in mm ####################')
for i in range(len(result)):
    confidence = result[i]['confidence']
    cx = int(confidence*100)
    if(cx>70):
        label = result[i]['label']
        if(label == 'Inhibition_ZONE'):
            tl = (result[i]['topleft']['x']),(result[i]['topleft']['y'])
            #print(tl)
            br = (result[i]['bottomright']['x']),(result[i]['bottomright']['y'])
            #print(br)
            #img = cv2.rectangle(img, tl, br, (255, 0, 0), 3)
            c_c_x = abs(tl[0]-br[0])
            c_c_x = int(c_c_x/2)
            c_c_y = abs(tl[1]-br[1])
            c_c_y = int(c_c_y/2)
            
            center_coordinates = (tl[0]+c_c_x,tl[1]+c_c_y)
            redius = abs(br[1]-tl[1])
            redius = int(redius/2)
            #print(redius)
            #print(center_coordinates)
            image = cv2.circle(img, center_coordinates, redius, (255, 0, 0), 2)
            iz +=1
            img = cv2.putText(img, str(iz),tl, cv2.FONT_HERSHEY_SIMPLEX, 1,(255,0,0), 2)
            count +=1
			# we took 6.5 pixels as 1 mm
            r_in_mm = 2*(redius/6.5)
            print('Inhibition_ZONE{}  :  {:.2f} mm'.format(iz,r_in_mm)) 
        else:
            tl = (result[i]['topleft']['x']),(result[i]['topleft']['y'])
            br = (result[i]['bottomright']['x']),(result[i]['bottomright']['y'])
            img = cv2.rectangle(img, tl, br, (0, 255, 0), 3)
            Ap +=1
            img = cv2.putText(img, str(Ap),tl, cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0), 2)
            count +=1

#print(i)
#print(count)
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
plt.imshow(img)

plt.show()

